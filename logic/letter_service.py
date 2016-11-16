from cStringIO import StringIO
import datetime
import re

import apilib
from dateutil import tz
import flask
from xhtml2pdf import pisa

from api import letter
from app import app
from config import constants
from database import db_models
from logic import db_to_api

R = db_models.Rep

TZ_EASTERN = tz.gettz('America/New_York')
PHONE_RE = re.compile('(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})')
EMAIL_RE = re.compile(r'([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)')

# xhtml2pdf logs errors like
# "missing explicit frame definition for content or just static frames"
# and it's unclear how to define frames to make this go away.
# If you don't define a handler, Python's logging module complains
# 'No handlers could be found for logger "xhtml2pdf"'
# So we register a NullHandler to shut it all up.
# If you want to see the actual warnings, change NullHandler to StreamHandler.
import logging
logging.getLogger('xhtml2pdf').addHandler(logging.NullHandler())

class LetterServiceImpl(letter.LetterService, apilib.ServiceImplementation):
    def __init__(self, **kwargs):
        pass

    def generate(self, req):
        html = self._generate_html(req)
        pdf_buffer = _create_pdf(html)
        return letter.GenerateLetterResponse(
            pdf_content=pdf_buffer.getvalue())

    def _generate_html(self, req):
        db_rep = R.query.get(req.rep_id)
        if not db_rep:
            raise _invalid_rep_id_exception(req.rep_id)
        return flask.render_template('pdf/letter.html',
            rep=db_to_api.db_rep_to_api(db_rep),
            body=req.body,
            name_and_address=req.name_and_address,
            sender_address=_make_sender_address(req.name_and_address),
            date_str=_date_str(),
            include_address_page=True,
            pdf_font_file=constants.PDF_FONT_FILE)

    def process_unhandled_exception(self, exception):
        # For debugging
        return True

def _invalid_rep_id_exception(rep_id):
    error = apilib.ApiError(code='UNKNOWN_REP', path='rep_id',
        message='No representative with rep_id %s could be found.' % rep_id)
    return apilib.ApiException.request_error([error])

def _create_pdf(pdf_data):
    if type(pdf_data) != unicode:
        pdf_data = StringIO(pdf_data.encode('utf-8'))
    pdf = StringIO()
    pisa.CreatePDF(
        pdf_data,
        dest=pdf,
        link_callback=lambda uri, rel: uri,
        encoding='utf-8')
    return pdf

def _date_str():
    return datetime.datetime.now(TZ_EASTERN).strftime('%B %-d, %Y')

def _make_sender_address(name_and_address):
    lines = []
    for line in name_and_address.split('\r\n'):
        if line and not PHONE_RE.search(line) and not EMAIL_RE.search(line):
            lines.append(line)
    return '\r\n'.join(lines)

# xhtml2pdf supports css white-space but not pre-line or pre-wrap,
# seemingly only pre. So we have to roll our own pre-line to get
# both wrapping and newlines.
@app.template_filter('newline_to_br')
def newline_to_br(s):
    s = s or ''
    escaped = unicode(app.jinja_env.filters['escape'](s))
    replaced = escaped.replace('\r\n', '<br/>')
    return app.jinja_env.filters['safe'](replaced)
