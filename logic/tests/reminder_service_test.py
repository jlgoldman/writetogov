import datetime
import unittest

from dateutil import tz
import mock

from api import reminder
from database import db
from database import db_models
from logic import reminder_logic
from logic import reminder_service
from testing import test_base

R = db_models.Reminder

def create_db_reminder(email, frequency=R.Frequency.WEEKLY, status=R.Status.ACTIVE):
    db_reminder = db_models.Reminder(
        email=email,
        frequency=frequency,
        status=status,
        last_contacted=datetime.datetime(2016, 2, 5, tzinfo=tz.tzutc()),
        time_created=datetime.datetime(2016, 2, 5, tzinfo=tz.tzutc()),
        time_updated=datetime.datetime(2016, 2, 5, tzinfo=tz.tzutc()))
    db.session.add(db_reminder)
    db.session.commit()
    return db_reminder

@mock.patch('util.sendgrid_.send_message')
class ReminderServiceTest(test_base.FakeDatabaseTest):
    def service(self):
        return reminder_service.ReminderServiceImpl()

    def test_create_weekly_reminder(self, mock_send_message):
        req = reminder.CreateReminderRequest(
            email='foo@foo.com',
            frequency=reminder.Frequency.WEEKLY)
        resp = self.service().invoke('create', req)
        self.assertEqual('SUCCESS', resp.response_code)
        db_reminder = R.query.filter(R.email == req.email).first()
        self.assertIsNotNone(db_reminder)
        self.assertEqual(req.email, db_reminder.email)
        self.assertEqual(R.Frequency.WEEKLY, db_reminder.frequency)
        self.assertEqual(R.Status.ACTIVE, db_reminder.status)
        self.assertIsNotNone(db_reminder.last_contacted)
        self.assertEqual(db_reminder.last_contacted, db_reminder.time_created)
        self.assertEqual(db_reminder.last_contacted, db_reminder.time_updated)
        mock_send_message.assert_called_once()

    def test_create_monthly_reminder(self, mock_send_message):
        req = reminder.CreateReminderRequest(
            email='foo@foo.com',
            frequency=reminder.Frequency.MONTHLY)
        resp = self.service().invoke('create', req)
        self.assertEqual('SUCCESS', resp.response_code)
        db_reminder = R.query.filter(R.email == req.email).first()
        self.assertIsNotNone(db_reminder)
        self.assertEqual(req.email, db_reminder.email)
        self.assertEqual(R.Frequency.MONTHLY, db_reminder.frequency)
        self.assertEqual(R.Status.ACTIVE, db_reminder.status)
        self.assertIsNotNone(db_reminder.last_contacted)
        self.assertEqual(db_reminder.last_contacted, db_reminder.time_created)
        self.assertEqual(db_reminder.last_contacted, db_reminder.time_updated)
        mock_send_message.assert_called_once()

    def test_normalize_email(self, mock_send_message):
        req = reminder.CreateReminderRequest(
            email='fOO@Foo.COM  ',
            frequency=reminder.Frequency.WEEKLY)
        resp = self.service().invoke('create', req)
        self.assertEqual('SUCCESS', resp.response_code)
        normalized_email = req.email.strip().lower()
        db_reminder = R.query.filter(R.email == normalized_email).first()
        self.assertIsNotNone(db_reminder)

    def test_create_reminder_for_existing_email(self, mock_send_message):
        email = 'blah@blah.com'
        existing_db_reminder = create_db_reminder(
            email, frequency=R.Frequency.MONTHLY, status=R.Status.UNSUBSCRIBED)
        original_time_created = existing_db_reminder.time_created
        original_time_updated = existing_db_reminder.time_updated
        original_last_contacted = existing_db_reminder.last_contacted

        req = reminder.CreateReminderRequest(
            email=email,
            frequency=reminder.Frequency.WEEKLY)
        resp = self.service().invoke('create', req)

        self.assertEqual('SUCCESS', resp.response_code)
        db_reminder = R.query.filter(R.email == req.email).first()
        self.assertIsNotNone(db_reminder)
        self.assertEqual(req.email, db_reminder.email)
        self.assertEqual(R.Frequency.WEEKLY, db_reminder.frequency)
        self.assertEqual(R.Status.ACTIVE, db_reminder.status)
        self.assertIsNotNone(db_reminder.last_contacted)
        self.assertGreater(db_reminder.last_contacted, original_last_contacted)
        self.assertGreater(db_reminder.time_updated, original_time_updated)
        self.assertEqual(db_reminder.time_created, original_time_created)
        mock_send_message.assert_called_once()

    def test_update_reminder_with_valid_token(self, mock_send_message):
        email = 'foo@foo.com'
        existing_db_reminder = create_db_reminder(
            email, frequency=R.Frequency.MONTHLY, status=R.Status.ACTIVE)
        original_time_created = existing_db_reminder.time_created
        original_time_updated = existing_db_reminder.time_updated
        original_last_contacted = existing_db_reminder.last_contacted

        req = reminder.UpdateReminderRequest(
            email=email,
            status=reminder.Status.UNSUBSCRIBED,
            token=reminder_logic.generate_email_token(email))
        resp = self.service().invoke('update', req)

        self.assertEqual('SUCCESS', resp.response_code)
        db_reminder = R.query.filter(R.email == req.email).first()
        self.assertIsNotNone(db_reminder)
        self.assertEqual(R.Status.UNSUBSCRIBED, db_reminder.status)
        self.assertGreater(db_reminder.time_updated, original_time_updated)
        self.assertEqual(db_reminder.last_contacted, original_last_contacted)
        self.assertEqual(db_reminder.time_created, original_time_created)
        mock_send_message.assert_not_called()

    def test_update_token_normalizes_email(self, mock_send_message):
        existing_db_reminder = create_db_reminder(
            'foo@foo.com', frequency=R.Frequency.MONTHLY, status=R.Status.ACTIVE)
        original_time_created = existing_db_reminder.time_created
        original_time_updated = existing_db_reminder.time_updated
        original_last_contacted = existing_db_reminder.last_contacted

        req = reminder.UpdateReminderRequest(
            email=' foo@FOO.COM',
            status=reminder.Status.UNSUBSCRIBED,
            token=reminder_logic.generate_email_token('FOO@foo.com '))
        resp = self.service().invoke('update', req)

        self.assertEqual('SUCCESS', resp.response_code)
        db_reminder = R.query.filter(R.email == req.email.strip().lower()).first()
        self.assertIsNotNone(db_reminder)
        self.assertEqual(R.Status.UNSUBSCRIBED, db_reminder.status)
        self.assertGreater(db_reminder.time_updated, original_time_updated)
        self.assertEqual(db_reminder.last_contacted, original_last_contacted)
        self.assertEqual(db_reminder.time_created, original_time_created)
        mock_send_message.assert_not_called()

    def test_update_reminder_with_invalid_token(self, mock_send_message):
        req = reminder.UpdateReminderRequest(
            email='foo@foo.com',
            status=reminder.Status.UNSUBSCRIBED,
            token='garbage')
        resp = self.service().invoke('update', req)

        self.assertEqual('REQUEST_ERROR', resp.response_code)
        self.assertEqual(1, len(resp.errors))
        self.assertEqual('INVALID_TOKEN', resp.errors[0].code)
        mock_send_message.assert_not_called()

    @mock.patch('util.time_.utcnow')
    def test_update_reminder_with_expired_token(self, mock_utcnow, mock_send_message):
        email = 'foo@foo.com'
        mock_utcnow.return_value = datetime.datetime(2010, 1, 1, tzinfo=tz.tzutc())
        token = reminder_logic.generate_email_token(email)

        req = reminder.UpdateReminderRequest(
            email=email,
            status=reminder.Status.UNSUBSCRIBED,
            token=token)
        mock_utcnow.return_value = datetime.datetime(2016, 11, 11, tzinfo=tz.tzutc())
        resp = self.service().invoke('update', req)

        self.assertEqual('REQUEST_ERROR', resp.response_code)
        self.assertEqual(1, len(resp.errors))
        self.assertEqual('INVALID_TOKEN', resp.errors[0].code)
        mock_send_message.assert_not_called()

if __name__ == '__main__':
    unittest.main()
