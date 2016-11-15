from flask import render_template
from flask import request

from app import app

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/letter_html')
def letter_html():
    from api import letter
    from logic import letter_service
    req = letter.GenerateLetterRequest(
        rep_id=61,
        body=request.args.get('body'),
        closing=request.args.get('closing'))
    service = letter_service.LetterServiceImpl()
    return service._generate_html(req)
