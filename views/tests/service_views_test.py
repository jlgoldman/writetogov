import json
import unittest

from api import rep
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

if __name__ == '__main__':
    unittest.main()
