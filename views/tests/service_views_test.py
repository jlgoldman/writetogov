import json
import unittest

import mock

from api import letter
from api import rep
from logic import letter_service
from testing import test_base
from views import service_views
assert service_views  # Silence pyflakes

class ServiceViewsTest(test_base.RealDatabaseTest):
    def send_json_post(self, url, json_data, headers=None):
        return self.client.post(url, data=json.dumps(json_data),
            content_type='application/json', headers=headers)

    def test_rep_service(self):
        req = rep.GetRepsRequest(rep_ids=[1])
        resp = self.send_json_post('/rep_service/get', req.to_json())
        self.assertEqual(200, resp.status_code)
        resp_js = json.loads(resp.data)
        self.assertEqual('SUCCESS', resp_js['response_code'])
        self.assertIsNotNone(resp_js['reps'])
        self.assertEqual(1, len(resp_js['reps']))

    @mock.patch.object(letter_service.LetterServiceImpl, 'generate_and_mail')
    def test_letter_service(self, mock_generate_and_mail):
        req = letter.GenerateAndMailLetterRequest(
            stripe_token='token',
            rep_id=1,
            body='body',
            name_and_address='name and adddress')
        mock_generate_and_mail.return_value = letter.GenerateAndMailLetterResponse()
        resp = self.send_json_post('/letter_service/generate_and_mail', req.to_json())
        self.assertEqual(200, resp.status_code)
        resp_js = json.loads(resp.data)
        self.assertEqual('SUCCESS', resp_js['response_code'])

if __name__ == '__main__':
    unittest.main()
