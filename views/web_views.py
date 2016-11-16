import apilib
import flask
from flask import json
from flask import render_template
from flask import request

from api import letter
from app import app
from config import constants
from logic import letter_service

AUTOCOMPLETE_DATA = json.load(open(constants.REP_AUTOCOMPLETE_DATA_FNAME))

@app.route('/')
@app.route('/district/<district_code>')
@app.route('/rep/<int:rep_id>')
@app.route('/state/<state_code>')
@app.route('/compose/<int:rep_id>')
def index(district_code=None, rep_id=None, state_code=None):
    return render_template('index.html', client_config=dict(
        rep_autocomplete_data=AUTOCOMPLETE_DATA,
        ))

@app.route('/generate_letter', methods=['POST'])
def generate_letter():
    req = letter.GenerateLetterRequest(
        rep_id=int(request.form['rep_id']),
        body=request.form['body'],
        closing=request.form['closing'])
    service = letter_service.LetterServiceImpl()
    resp = service.invoke('generate', req)
    if not resp.response_code == 'SUCCESS':
        app.logger.error('Error generating PDF letter: %s', resp)
        response_code = 400 if resp.response_code == apilib.ResponseCode.REQUEST_ERROR else 500
        return 'There was an error generating your letter', response_code
    return flask.Response(resp.pdf_content, mimetype='application/pdf')

# For debugging only
@app.route('/letter_html')
def letter_html():
    req = letter.GenerateLetterRequest(
        rep_id=61,
        body=request.args.get('body'),
        closing=request.args.get('closing'))
    service = letter_service.LetterServiceImpl()
    return service._generate_html(req)
