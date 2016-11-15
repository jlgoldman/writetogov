import apilib
import flask
from flask import render_template
from flask import request

from api import letter
from app import app
from logic import letter_service

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_letter', methods=['POST'])
def generate_letter():
    req = letter.GenerateLetterRequest(**request.json)
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
