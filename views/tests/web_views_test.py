import unittest

import mock

from logic import reminder_service
from testing import test_base
from views import web_views
assert web_views  # Silence pyflakes

class WebViewsTest(test_base.RealDatabaseTest):
    def test_heartbeat(self):
        resp = self.client.get('/')
        self.assertEqual(200, resp.status_code)
        resp = self.client.get('/district/CA11')
        self.assertEqual(200, resp.status_code)
        resp = self.client.get('/compose/20')
        self.assertEqual(200, resp.status_code)

    def test_generate_letter_pdf(self):
        resp = self.client.post('/letter', data=dict(
            rep_id='61',
            body='hello world',
            name_and_address='Bob Smith\nSan Francisco, CA'))
        self.assertEqual(200, resp.status_code)
        self.assertEqual('application/pdf', resp.headers.get('Content-Type'))
        self.assertIsNotNone(resp.data)

    @mock.patch('app.app.logger.error')
    def test_generate_letter_with_invalid_params(self, mock_log_error):
        resp = self.client.post('/letter', data=dict(
            rep_id='-1',
            body='hello world',
            name_and_address='Bob Smith\nSan Francisco, CA'))
        self.assertEqual(400, resp.status_code)
        mock_log_error.assert_called_once()

    @mock.patch.object(reminder_service.ReminderServiceImpl, 'update')
    def test_reminder_unsubscribe(self, mock_update):
        resp = self.client.get('/reminder/unsubscribe?email=foo@foo.com&token=blah')
        self.assertEqual(200, resp.status_code)
        mock_update.assert_called_once()
        update_req = mock_update.call_args[0][0]
        self.assertEqual('foo@foo.com', update_req.email)
        self.assertEqual('blah', update_req.token)
        self.assertEqual('UNSUBSCRIBED', update_req.status)

if __name__ == '__main__':
    unittest.main()
