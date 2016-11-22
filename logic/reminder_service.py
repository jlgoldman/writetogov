import urllib2

import apilib
from flask import render_template

from api import reminder
from database import db
from database import db_models
from logic import reminder_logic
from util import sendgrid_
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

class ReminderServiceImpl(reminder.ReminderService, apilib.ServiceImplementation):
    def __init__(self, **kwargs):
        pass

    def create(self, req):
        email = req.email.strip().lower()
        now = time_.utcnow()
        existing_db_reminder = R.query.filter(R.email == email).first()
        db_frequency = API_FREQUENCY_TO_DB[req.frequency]
        if existing_db_reminder:
            existing_db_reminder.frequency = db_frequency
            existing_db_reminder.status = R.Status.ACTIVE
            existing_db_reminder.last_contacted = now
            existing_db_reminder.time_updated = now
        else:
            db_reminder = db_models.Reminder(
                email=email,
                frequency=db_frequency,
                status=R.Status.ACTIVE,
                last_contacted=now,
                time_created=now,
                time_updated=now)
            db.session.add(db_reminder)
        db.session.commit()
        _send_confirmation_email(email, db_frequency)
        return reminder.CreateReminderResponse()

    def update(self, req):
        if not reminder_logic.verify_email_token(req.token, req.email):
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

def _send_confirmation_email(email, frequency):
    unsubscribe_url = reminder_logic.generate_unsubscribe_url(email)
    subject = 'Confirmation of periodic reminders'

    html = render_template('email/reminder_confirmation.html',
        subject=subject,
        frequency=frequency,
        unsubscribe_url=unsubscribe_url)
    text = render_template('email/reminder_confirmation.txt',
        frequency=frequency,
        unsubscribe_url=unsubscribe_url)

    retries = 3
    while retries > 0:
        try:
            return sendgrid_.send_message(
                subject=subject,
                body_text=text,
                body_html=html,
                recipients=[email])
        except urllib2.URLError:
            retries -= 1
            if retries == 0:
                raise

def _invalid_token_exception():
    error = apilib.ApiError(code='INVALID_TOKEN', path='token',
        message='The provided token is either invalid or expired.')
    return apilib.ApiException.request_error([error])
