from cStringIO import StringIO
import datetime
import re

import apilib
from dateutil import parser as dateutil_parser
from dateutil import tz
import flask
import lob
from PyPDF2 import PdfFileMerger
import stripe
import usaddress
from xhtml2pdf import pisa

from api import letter
from app import app
from config import constants
from database import db
from database import db_models
from logic import db_to_api
from util import fips
from util import time_

stripe.api_key = constants.STRIPE_SECRET_KEY
lob.api_key = constants.LOB_API_KEY

R = db_models.Rep

TZ_EASTERN = tz.gettz('America/New_York')
PHONE_RE = re.compile('(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})')
EMAIL_RE = re.compile(r'([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)')
ZIP4_LINE_RE = re.compile('\d{5}-\d{4}')
ADDRESS_DC_PARSE_RE = re.compile('(\d+\w?)\s+(.+)\s+Washington,?\s+DC,?\s+(\d+)')

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
        db_rep = R.query.get(req.rep_id)
        html = self._generate_html(req, db_rep)
        pdf_buffer = _create_pdf(html)

        if req.include_address_page:
            address_page_html = self._generate_address_page_html(req, db_rep)
            address_pdf_buffer = _create_pdf(address_page_html)
            pdf_buffer = merge_pdf_buffers(pdf_buffer, address_pdf_buffer)

        return letter.GenerateLetterResponse(
            pdf_content=pdf_buffer.getvalue())

    def generate_and_mail(self, req):
        db_rep = R.query.get(req.rep_id)
        html = self._generate_html(req, db_rep)
        pdf_buffer = _create_pdf(html)

        api_rep = db_to_api.db_rep_to_api(db_rep)
        description = 'Letter to %s %s %s' % (
            api_rep.title, api_rep.first_name, api_rep.last_name)
        stripe_charge = self._charge_via_stripe(req.stripe_token, description)
        now = time_.utcnow()
        db_rep_mailing = db_models.RepMailing(
            rep_id=req.rep_id,
            email=req.email.strip().lower(),
            stripe_charge_id=stripe_charge.id,
            time_created=now,
            time_updated=now)
        db.session.add(db_rep_mailing)
        db.session.commit()

        lob_response = self._make_lob_request(
            pdf_buffer, api_rep, description, req.name_and_address)
        db_rep_mailing.lob_letter_id = lob_response['id']
        db_rep_mailing.time_updated = time_.utcnow()
        db.session.commit()

        return letter.GenerateAndMailLetterResponse(
            expected_delivery_date=dateutil_parser.parse(
                lob_response['expected_delivery_date']).strftime('%B %-d'),
            lob_pdf_url=lob_response['url'])

    def _generate_html(self, req, db_rep=None):
        db_rep = db_rep or R.query.get(req.rep_id)
        if not db_rep:
            raise _invalid_rep_id_exception(req.rep_id)
        return flask.render_template('pdf/letter.html',
            rep=db_to_api.db_rep_to_api(db_rep),
            body=req.body,
            name_and_address=req.name_and_address,
            date_str=_date_str(),
            pdf_font_file=constants.PDF_FONT_FILE)

    def _generate_address_page_html(self, req, db_rep=None):
        db_rep = db_rep or R.query.get(req.rep_id)
        if not db_rep:
            raise _invalid_rep_id_exception(req.rep_id)
        return flask.render_template('pdf/address_page.html',
            rep=db_to_api.db_rep_to_api(db_rep),
            sender_address=_make_sender_address(req.name_and_address),
            pdf_font_file=constants.PDF_FONT_FILE)

    def _charge_via_stripe(self, stripe_token, description):
        try:
            return stripe.Charge.create(
                amount=150,
                currency='usd',
                source=stripe_token,
                description=description)
        except stripe.error.CardError as e:
            app.logger.error('Stripe charge error: %s', e)
            raise _charge_error_exception('There was an error charging your card: %s' % e.message)

    def _make_lob_request(self, pdf_buffer, api_rep, description, send_name_and_address):
        try:
            return lob.Letter.create(
              description=description,
              to_address=_api_rep_address_to_lob_address(api_rep),
              from_address=_sender_name_and_address_to_lob_address(send_name_and_address),
              file=StringIO(pdf_buffer.getvalue()),
              address_placement='insert_blank_page',
              double_sided=True,
              color=False)
        except lob.error.LobError as e:
            app.logger.error('Lob API error: %s', e)
            raise _lob_error_exception(
                'There was an error submitting your letter to be mailed. Please contact info@writetogov.com.')

    def process_unhandled_exception(self, exception):
        # For debugging
        return True

def merge_pdf_buffers(*buffers):
    merger = PdfFileMerger()
    for pdf_buffer in buffers:
        merger.append(pdf_buffer)
    output = StringIO()
    merger.write(output)
    return output

def _invalid_rep_id_exception(rep_id):
    error = apilib.ApiError(code='UNKNOWN_REP', path='rep_id',
        message='No representative with rep_id %s could be found.' % rep_id)
    return apilib.ApiException.request_error([error])

def _charge_error_exception(message):
    error = apilib.ApiError(code='CHARGE_ERROR', path='stripe_token',
        message=message)
    return apilib.ApiException.request_error([error])

def _lob_error_exception(message):
    error = apilib.ApiError(code='LETTER_ERROR', message=message)
    return apilib.ApiException.server_error([error])

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
    delimiter = '\r\n' if '\r\n' in name_and_address else '\n'
    for line in name_and_address.split(delimiter):
        is_phone_line = PHONE_RE.search(line) and not ZIP4_LINE_RE.search(line)
        if line and not is_phone_line and not EMAIL_RE.search(line):
            lines.append(line)
    return '\r\n'.join(lines)

def _api_rep_address_to_lob_address(api_rep):
    match = ADDRESS_DC_PARSE_RE.match(api_rep.address_dc)
    return {
      'name': '%s %s %s' % (api_rep.title, api_rep.first_name, api_rep.last_name),
      'address_line1': '%s %s' % (match.group(1), match.group(2)),
      'address_city': 'Washington',
      'address_state': 'DC',
      'address_zip': match.group(3),
      'address_country': 'US',
    }

def _sender_name_and_address_to_lob_address(name_and_address):
    # Remove phone and email
    lines = _make_sender_address(name_and_address).split('\r\n')
    parsed = usaddress.parse(', '.join(lines[1:]))
    line1_parts = []
    place_name_parts = []
    state = None
    zipcode = None
    for part, part_type in parsed:
        if part_type == 'PlaceName':
            place_name_parts.append(part.rstrip(','))
        elif part_type == 'StateName' and not state:
            state = part
        elif part_type == 'ZipCode':
            zipcode = part
        elif part_type == 'ZipPlus4' and zipcode and len(zipcode) == 5:
            zipcode = '%s-%s' % (zipcode, part)
        else:
            line1_parts.append(part.rstrip(','))
    if state and len(state) > 2:
        state = fips.get_state_code_for_name(state)
    return {
        'name': lines[0] if lines else None,
        'address_line1': ' '.join(line1_parts),
        'address_city': ' '.join(place_name_parts),
        'address_state': state.upper() if state else None,
        'address_zip': zipcode,
        'address_country': 'US',
    }

# xhtml2pdf supports css white-space but not pre-line or pre-wrap,
# seemingly only pre. So we have to roll our own pre-line to get
# both wrapping and newlines.
@app.template_filter('newline_to_br')
def newline_to_br(s):
    s = s or ''
    escaped = unicode(app.jinja_env.filters['escape'](s))
    replaced = escaped.replace('\r\n', '<br/>')
    return app.jinja_env.filters['safe'](replaced)
