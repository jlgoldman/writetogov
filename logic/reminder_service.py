import calendar

import apilib

from api import reminder
from database import db
from database import db_models
from util import crypto
from util import time_

R = db_models.Reminder

API_FREQUENCY_TO_DB = {
    reminder.Frequency.WEEKLY: R.Frequency.WEEKLY,
    reminder.Frequency.MONTHLY: R.Frequency.MONTHLY,
}

API_STATUS_TO_DB = {
    reminder.Status.ACTIVE: R.Status.ACTIVE,
    reminder.Status.UNSUBSCRIBED: R.Status.UNSUBSCRIBED,
}

TOKEN_EXPIRY_SECS = 60 * 60 * 24 * 7  # 1 week

class ReminderServiceImpl(reminder.ReminderService, apilib.ServiceImplementation):
    def __init__(self, **kwargs):
        pass

    def create(self, req):
        email = req.email.strip().lower()
        now = time_.utcnow()
        existing_db_reminder = R.query.filter(R.email == email).first()
        if existing_db_reminder:
            existing_db_reminder.frequency = API_FREQUENCY_TO_DB[req.frequency]
            existing_db_reminder.status = R.Status.ACTIVE
            existing_db_reminder.last_contacted = now
            existing_db_reminder.time_updated = now
        else:
            db_reminder = db_models.Reminder(
                email=email,
                frequency=API_FREQUENCY_TO_DB[req.frequency],
                status=R.Status.ACTIVE,
                last_contacted=now,
                time_created=now,
                time_updated=now)
            db.session.add(db_reminder)
        db.session.commit()
        # TODO: Send confirmation email
        return reminder.CreateReminderResponse()

    def update(self, req):
        if not verify_email_token(req.token, req.email):
            raise _invalid_token_exception()
        email = req.email.strip().lower()
        now = time_.utcnow()
        existing_db_reminder = R.query.filter(R.email == email).first()
        if existing_db_reminder:
            existing_db_reminder.status = API_STATUS_TO_DB[req.status]
            existing_db_reminder.time_updated = now
        db.session.commit()
        return reminder.UpdateReminderResponse()

    def process_unhandled_exception(self, exception):
        # For debugging
        return True

def generate_email_token(email):
    email = email.strip().lower()
    timestamp = _current_timestamp()
    msg = '%s|||%d' % (email, timestamp)
    return crypto.encrypt_with_salt(msg)

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

def _current_timestamp():
    return calendar.timegm(time_.utcnow().timetuple())

def _invalid_token_exception():
    error = apilib.ApiError(code='INVALID_TOKEN', path='token',
        message='The provided token is either invalid or expired.')
    return apilib.ApiException.request_error([error])
