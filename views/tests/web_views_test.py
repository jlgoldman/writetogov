from cStringIO import StringIO
import unittest

import mock
from PyPDF2 import PdfFileReader

from logic import reminder_service
from testing import test_base
from testing import test_data
from util import ids
from views import web_views
assert web_views  # Silence pyflakes

pelosi = test_data.RepData.nancy_pelosi

class WebViewsTest(test_base.DatabaseWithTestdataTest):
    def test_heartbeat(self):
        resp = self.client.get('/')
        self.assertEqual(200, resp.status_code)
        resp = self.client.get('/district/%s' % test_data.DistrictData.wy00.district_code)
        self.assertEqual(200, resp.status_code)
        resp = self.client.get('/compose/%s' % pelosi.rep_id)
        self.assertEqual(200, resp.status_code)

        resp = self.client.get('/robots.txt')
        self.assertEqual(200, resp.status_code)
        resp = self.client.get('/sitemap.txt')
        self.assertEqual(200, resp.status_code)

    def test_generate_letter_pdf(self):
        resp = self.client.post('/letter', data=dict(
            rep_id=str(pelosi.rep_id),
            body='hello world',
            name_and_address='Bob Smith\nSan Francisco, CA',
            include_address_page='1'))
        self.assertEqual(200, resp.status_code)
        self.assertEqual('application/pdf', resp.headers.get('Content-Type'))
        self.assertIsNotNone(resp.data)

        pdf_reader = PdfFileReader(StringIO(resp.data))
        self.assertEqual(2, pdf_reader.getNumPages())

    def test_generate_letter_pdf_without_address_page(self):
        resp = self.client.post('/letter', data=dict(
            rep_id=str(pelosi.rep_id),
            body='hello world',
            name_and_address='Bob Smith\nSan Francisco, CA',
            include_address_page='0'))
        self.assertEqual(200, resp.status_code)
        self.assertEqual('application/pdf', resp.headers.get('Content-Type'))
        self.assertIsNotNone(resp.data)

        pdf_reader = PdfFileReader(StringIO(resp.data))
        self.assertEqual(1, pdf_reader.getNumPages())

    @mock.patch('app.app.logger.error')
    def test_generate_letter_with_invalid_params(self, mock_log_error):
        resp = self.client.post('/letter', data=dict(
            rep_id='-1',
            body='hello world',
            name_and_address='Bob Smith\nSan Francisco, CA',
            include_address_page='1'))
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

    def test_get_issue_page(self):
        issue_data = test_data.IssueData.issue1
        resp = self.client.get('/issue/%s' % ids.public_id(issue_data.issue_id))
        self.assertEqual(200, resp.status_code)

    def test_create_issue_page(self):
        resp = self.client.get('/issue/create')
        self.assertEqual(200, resp.status_code)

    def test_edit_issue_page(self):
        issue_data = test_data.IssueData.issue1
        resp = self.client.get('/issue/%s/edit?token=issuetoken' %
            ids.public_id(issue_data.issue_id))
        self.assertEqual(200, resp.status_code)
        self.assertTrue('issuetoken' in resp.data)
        self.assertTrue(issue_data.description in resp.data)

if __name__ == '__main__':
    unittest.main()
