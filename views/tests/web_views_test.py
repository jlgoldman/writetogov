import json
import unittest

import mock

from api import letter
from testing import test_base
from views import web_views
assert web_views  # Silence pyflakes

class WebViewsTest(test_base.RealDatabaseTest):
    def send_json_post(self, url, json_data, headers=None):
        return self.client.post(url, data=json.dumps(json_data),
            content_type='application/json', headers=headers)

    def test_heartbeat(self):
        resp = self.client.get('/')
        self.assertEqual(200, resp.status_code)

    def test_generate_letter_pdf(self):
        req = letter.GenerateLetterRequest(
            rep_id=61,
            body='hello world',
            closing='Bob Smith\nSan Francisco, CA')
        resp = self.send_json_post('/generate_letter', req.to_json())
        self.assertEqual(200, resp.status_code)
        self.assertEqual('application/pdf', resp.headers.get('Content-Type'))
        self.assertIsNotNone(resp.data)

    @mock.patch('app.app.logger.error')
    def test_generate_letter_with_invalid_params(self, mock_log_error):
        req = letter.GenerateLetterRequest(
            rep_id=-1,
            body='hello world',
            closing='Bob Smith\nSan Francisco, CA')
        resp = self.send_json_post('/generate_letter', req.to_json())
        self.assertEqual(400, resp.status_code)
        mock_log_error.assert_called_once()

if __name__ == '__main__':
    unittest.main()
