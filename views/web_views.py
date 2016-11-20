import functools

import apilib
import flask
from flask import json
from flask import render_template
from flask import request

from api import letter
from app import app
from config import constants
from logic import api_shortcuts
from logic import letter_service
from util import urls

AUTOCOMPLETE_DATA = json.load(open(constants.REP_AUTOCOMPLETE_DATA_FNAME))

class PageType(object):
    HOME = 1
    DISTRICT = 2
    COMPOSE = 3

@app.route('/')
@app.route('/district/<district_code>')
@app.route('/compose/<int:rep_id>')
def index(district_code=None, rep_id=None):
    page_type = PageType.HOME
    if request.path.startswith('/district/'):
        page_type = PageType.DISTRICT
    elif request.path.startswith('/compose/'):
        page_type = PageType.COMPOSE

    api_rep, lookup_resp = None, None
    if district_code:
        lookup_resp = api_shortcuts.lookup_reps_by_district_code(district_code)
    elif rep_id:
        api_rep = api_shortcuts.get_rep_by_id(rep_id)
        if not api_rep:
            return 'Invalid representative id', 404

    return render_template('index.html',
        page_type=page_type,
        PageType=PageType,
        rep=api_rep,
        lookup_response=lookup_resp,
        google_maps_api_key=constants.GOOGLE_MAPS_API_KEY,
        client_config=dict(
            rep=api_rep.to_json() if api_rep else None,
            lookup_response=lookup_resp.to_json() if lookup_resp else None,
            rep_autocomplete_data=AUTOCOMPLETE_DATA,
        ))

@app.route('/letter', methods=['POST'])
def generate_letter():
    req = letter.GenerateLetterRequest(
        rep_id=int(request.form['rep_id']),
        body=request.form['body'],
        name_and_address=request.form['name_and_address'],
        include_address_page=True)
    service = letter_service.LetterServiceImpl()
    resp = service.invoke('generate', req)
    if not resp.response_code == 'SUCCESS':
        app.logger.error('Error generating PDF letter: %s', resp)
        response_code = 400 if resp.response_code == apilib.ResponseCode.REQUEST_ERROR else 500
        return 'There was an error generating your letter', response_code
    return flask.Response(resp.pdf_content, mimetype='application/pdf',
        headers={'Content-Disposition': 'attachment; filename=letter.pdf'})

@app.route('/reminder/unsubscribe')
def reminder_unsubscribe():
    update_response = api_shortcuts.unsubscribe_from_reminder(
        request.args['email'], request.args['token'])
    success = update_response.response_code == 'SUCCESS'
    has_invalid_token = update_response.errors and update_response.errors[0].code == 'INVALID_TOKEN'
    return render_template('reminder_unsubscribe.html',
        success=success, has_invalid_token=has_invalid_token)

@app.route('/robots.txt')
def robots_txt():
    return text_data_file_response('robots.txt')

@app.route('/sitemap.txt')
def sitemap_txt():
    return text_data_file_response('sitemap.txt')

def text_data_file_response(filename):
    text = open(constants.abspath('data/%s' % filename)).read()
    return flask.Response(text, mimetype='text/plain')


# Internal monitoring servlets

def internal_monitoring_only(fn):
    @functools.wraps(fn)
    def decorated(*args, **kwargs):
        if ('ELB-HealthChecker' in request.user_agent.string) or is_internal():
            return fn(*args, **kwargs)
        return '', 404
    return decorated

@app.route('/healthz')
@internal_monitoring_only
def healthz():
    return 'ok'

def is_internal():
    return request.remote_addr in constants.INTERNAL_IPS

@app.context_processor
def inject_extended_template_builtins():
    return dict(
        canonical_url=urls.absurl(request.url))


if constants.DEBUG:
    # For debugging only
    @app.route('/letter_debug', methods=['POST'])
    def generate_letter_debug():
        req = letter.GenerateLetterRequest(
            rep_id=int(request.form['rep_id']),
            body=request.form['body'],
            name_and_address=request.form['name_and_address'])
        service = letter_service.LetterServiceImpl()
        return service._generate_html(req)
