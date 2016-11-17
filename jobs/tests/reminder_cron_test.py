import datetime
import unittest

from dateutil import relativedelta
from dateutil import tz
import mock

from database import db
from database import db_models
from jobs import reminder_cron
from testing import test_base
from util import time_

R = db_models.Reminder

def create_db_reminder(email, last_contacted=None,
    frequency=R.Frequency.WEEKLY, status=R.Status.ACTIVE):
    db_reminder = db_models.Reminder(
        email=email,
        frequency=frequency,
        status=status,
        last_contacted=last_contacted,
        time_created=datetime.datetime(2016, 2, 5, tzinfo=tz.tzutc()),
        time_updated=datetime.datetime(2016, 2, 5, tzinfo=tz.tzutc()))
    db.session.add(db_reminder)
    db.session.commit()
    return db_reminder

def date_days_ago(days):
    return time_.utcnow() - relativedelta.relativedelta(days=days)

@mock.patch('jobs.reminder_cron.send_message')
class ReminderCronTest(test_base.FakeDatabaseTest):
    def test_reminders_sent(self, mock_send_message):
        create_db_reminder('weekly@weekly.com',
            frequency=R.Frequency.WEEKLY,
            last_contacted=date_days_ago(8))
        create_db_reminder('monthly@monthly.com',
            frequency=R.Frequency.MONTHLY,
            last_contacted=date_days_ago(35))

        reminder_cron.main()

        self.assertEqual(2, mock_send_message.call_count)
        db_reminders = R.query \
            .filter(R.email.in_(['weekly@weekly.com', 'monthly@monthly.com'])) \
            .all()
        self.assertEqual(2, len(db_reminders))
        now = time_.utcnow()
        self.assertLess((now - db_reminders[0].last_contacted).total_seconds(), 1)
        self.assertLess((now - db_reminders[1].last_contacted).total_seconds(), 1)

    def test_unsubscribed_reminders_ignored(self, mock_send_message):
        create_db_reminder('weekly@weekly.com',
            status=R.Status.UNSUBSCRIBED,
            frequency=R.Frequency.WEEKLY,
            last_contacted=date_days_ago(8))
        create_db_reminder('monthly@monthly.com',
            status=R.Status.UNSUBSCRIBED,
            frequency=R.Frequency.MONTHLY,
            last_contacted=date_days_ago(35))

        reminder_cron.main()

        mock_send_message.assert_not_called()

    def test_recently_contacted_reminders_ignored(self, mock_send_message):
        create_db_reminder('weekly@weekly.com',
            frequency=R.Frequency.WEEKLY,
            last_contacted=date_days_ago(6))
        create_db_reminder('monthly@monthly.com',
            frequency=R.Frequency.MONTHLY,
            last_contacted=date_days_ago(27))

        reminder_cron.main()

        mock_send_message.assert_not_called()

if __name__ == '__main__':
    unittest.main()
