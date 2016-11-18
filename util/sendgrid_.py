import pprint

import sendgrid

from config import constants

DEFAULT_SENDER_EMAIL = 'info@writetogov.com'
DEFAULT_SENDER_NAME = 'Write to the Government'

def send_message(subject, body_text, body_html, recipients,
    sender_email=DEFAULT_SENDER_EMAIL, sender_name=DEFAULT_SENDER_NAME,
    ccs=None, bccs=None,
    send=True, print_data=False):
    sg_client = sendgrid.SendGridAPIClient(apikey=constants.SENDGRID_API_KEY)
    personalizations = [
        {'to': [{'email': email} for email in recipients]}
    ]
    if ccs:
        personalizations.append({'cc': [{'email': email} for email in ccs]})
    if bccs:
        personalizations.append({'bcc': [{'email': email} for email in bccs]})
    data = {
        'subject': subject,
        'from': {'email': sender_email, 'name': sender_name},
        'content': [
            {'type': 'text/plain', 'value': body_text},
            {'type': 'text/html',  'value': body_html},
        ],
        'personalizations': personalizations,
        }
    if print_data:
        pprint.pprint(data)
    if send:
        return sg_client.client.mail.send.post(request_body=data)
