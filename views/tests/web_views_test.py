import json
import unittest

import mock

from api import letter
from testing import test_base
from views import web_views
assert web_views  # Silence pyflakes

class WebViewsTest(test_base.RealDatabaseTest):
    def test_heartbeat(self):
        resp = self.client.get('/')
        self.assertEqual(200, resp.status_code)
        resp = self.client.get('/district/CA11')
        self.assertEqual(200, resp.status_code)
        resp = self.client.get('/rep/12')
        self.assertEqual(200, resp.status_code)
        resp = self.client.get('/state/FL')
        self.assertEqual(200, resp.status_code)
        resp = self.client.get('/compose/20')
        self.assertEqual(200, resp.status_code)

    def test_generate_letter_pdf(self):
        resp = self.client.post('/generate_letter', data=dict(
            rep_id='61',
            body='hello world',
            closing='Bob Smith\nSan Francisco, CA'))
        self.assertEqual(200, resp.status_code)
        self.assertEqual('application/pdf', resp.headers.get('Content-Type'))
        self.assertIsNotNone(resp.data)

    @mock.patch('app.app.logger.error')
    def test_generate_letter_with_invalid_params(self, mock_log_error):
        resp = self.client.post('/generate_letter', data=dict(
            rep_id='-1',
            body='hello world',
            closing='Bob Smith\nSan Francisco, CA'))
        self.assertEqual(400, resp.status_code)
        mock_log_error.assert_called_once()

if __name__ == '__main__':
    unittest.main()
