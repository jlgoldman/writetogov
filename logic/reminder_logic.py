import calendar

from util import crypto
from util import time_
from util import urls

TOKEN_EXPIRY_SECS = 60 * 60 * 24 * 7  # 1 week

def generate_unsubscribe_url(email):
    token = generate_email_token(email)
    return urls.absurl(urls.append_params('/reminder/unsubscribe', dict(
        email=email, token=token)))

def verify_email_token(token, email):
    email = email.strip().lower()
    try:
        msg = crypto.decrypt_with_salt(token)
    except:
        return False
    parts = msg.split('|||')
    token_email, token_timestamp = parts[0], int(parts[1])
    return (token_email == email
        and _current_timestamp() - token_timestamp < TOKEN_EXPIRY_SECS)

def generate_email_token(email):
    email = email.strip().lower()
    timestamp = _current_timestamp()
    msg = '%s|||%d' % (email, timestamp)
    return crypto.encrypt_with_salt(msg)

def _current_timestamp():
    return calendar.timegm(time_.utcnow().timetuple())
