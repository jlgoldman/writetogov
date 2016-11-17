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

AUTOCOMPLETE_DATA = json.load(open(constants.REP_AUTOCOMPLETE_DATA_FNAME))

@app.route('/')
@app.route('/district/<district_code>')
@app.route('/compose/<int:rep_id>')
def index(district_code=None, rep_id=None):
    api_rep, lookup_resp, title = None, None, None
    if district_code:
        lookup_resp = api_shortcuts.lookup_reps_by_district_code(district_code)
        if lookup_resp and lookup_resp.house_rep:
            title = '%s\'s %s District - Write to the Government' % (
                lookup_resp.house_rep.state_name, lookup_resp.house_rep.district_ordinal)
    elif rep_id:
        api_rep = api_shortcuts.get_rep_by_id(rep_id)
        if not api_rep:
            return 'Invalid representative id', 404
        title = 'Write to %s %s %s - Write to the Government' % (
            api_rep.title, api_rep.first_name, api_rep.last_name)

    return render_template('index.html',
        title=title,
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
    return flask.Response(resp.pdf_content, mimetype='application/pdf')

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
