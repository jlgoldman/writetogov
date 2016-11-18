import itertools

from dateutil import relativedelta
from flask import render_template

from database import db
from database import db_models
from logic import reminder_service
from util import sendgrid_
from util import time_
from util import urls

R = db_models.Reminder

def main():
    now = time_.utcnow()
    one_week_ago = now - relativedelta.relativedelta(weeks=1)
    one_month_ago = now - relativedelta.relativedelta(months=1)
    weekly_reminders = R.query \
        .filter(R.status == R.Status.ACTIVE) \
        .filter(R.frequency == R.Frequency.WEEKLY) \
        .filter(R.last_contacted <= one_week_ago)
    monthly_reminders = R.query \
        .filter(R.status == R.Status.ACTIVE) \
        .filter(R.frequency == R.Frequency.MONTHLY) \
        .filter(R.last_contacted <= one_month_ago)
    for db_reminder in itertools.chain(weekly_reminders, monthly_reminders):
        try:
            send_reminder_email(db_reminder.email, db_reminder.frequency)
            db_reminder.last_contacted = time_.utcnow()
            db.session.commit()
        except Exception as e:
            print 'Error sending reminder email: %s' % e

def send_reminder_email(email, frequency):
    token = reminder_service.generate_email_token(email)
    unsubscribe_url = urls.absurl(urls.append_params('/reminder/unsubscribe', dict(
        email=email, token=token)))
    subject = 'It\'s time to write to your elected representatives'

    html = render_template('email/reminder.html',
        subject=subject,
        frequency=frequency,
        unsubscribe_url=unsubscribe_url)
    text = render_template('email/reminder.txt',
        frequency=frequency,
        unsubscribe_url=unsubscribe_url)

    sendgrid_.send_message(
        subject=subject,
        body_text=text,
        body_html=html,
        recipients=[email])

if __name__ == '__main__':
    from tools import db_utils
    with db_utils.request_context():
        main()
