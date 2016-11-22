import unittest

import mock

from api import issue
from database import db
from database import db_models
from logic import issue_service
from testing import test_base
from testing import test_data

I = db_models.Issue
RD = test_data.RepData

@mock.patch('util.sendgrid_.send_message')
class IssueServiceTest(test_base.DatabaseWithTestdataTest):
    def service(self):
        return issue_service.IssueServiceImpl()

    def assertNumApiErrors(self, num_errors, api_response):
        self.assertIsNotNone(api_response.errors, 'Expected %d errors but found none' % num_errors)
        self.assertEqual(num_errors, len(api_response.errors),
            'Expected %d errors but found %d' % (num_errors, len(api_response.errors)))

    def assertHasApiError(self, api_response, code, path):
        self.assertIsNotNone(api_response.errors, 'Expected error with code %s but found no errors' % code)
        for api_error in api_response.errors:
            if api_error.code == code and api_error.path == path:
                return
        self.fail('Expected error with code %s at path "%s"' % (code, path))

    def test_create_new_issue(self, mock_send_message):
        req = issue.CreateIssueRequest(
            creator_email='foo@foo.com',
            issue=issue.Issue(
                creator_name='Bob Smith',
                title='Issue Title',
                description='Issue description',
                rep_ids=[RD.nancy_pelosi.rep_id, RD.michael_enzi.rep_id]))

        resp = self.service().invoke('create', req)
        self.assertEqual('SUCCESS', resp.response_code)
        self.assertIsNotNone(resp.issue)
        self.assertIsNotNone(resp.issue.issue_id)
        self.assertEqual(req.issue.creator_name, resp.issue.creator_name)
        self.assertEqual(req.issue.title, resp.issue.title)
        self.assertEqual(req.issue.description, resp.issue.description)
        self.assertEqual(req.issue.rep_ids, resp.issue.rep_ids)
        self.assertIsNotNone(resp.issue.url)

        db_issue = I.query.get(resp.issue.issue_id)
        self.assertIsNotNone(db_issue)
        self.assertEqual(req.creator_email, db_issue.creator_email)
        self.assertEqual(req.issue.creator_name, db_issue.creator_name)
        self.assertEqual(req.issue.title, db_issue.title)
        self.assertEqual(req.issue.description, db_issue.description)
        self.assertEqual(req.issue.rep_ids, db_issue.rep_ids)
        self.assertIsNotNone(db_issue.time_created)
        self.assertIsNotNone(db_issue.time_updated)

        mock_send_message.assert_called_once()

    def test_create_new_issue_with_optional_fields(self, mock_send_message):
        req = issue.CreateIssueRequest(
            creator_email='foo@foo.com',
            issue=issue.Issue(
                title='Issue Title',
                description='Issue description'))

        resp = self.service().invoke('create', req)
        self.assertEqual('SUCCESS', resp.response_code)
        self.assertIsNotNone(resp.issue)
        self.assertIsNotNone(resp.issue.issue_id)
        self.assertIsNone(resp.issue.creator_name)
        self.assertEqual(req.issue.title, resp.issue.title)
        self.assertEqual(req.issue.description, resp.issue.description)
        self.assertIsNone(resp.issue.rep_ids)

        db_issue = I.query.get(resp.issue.issue_id)
        self.assertIsNotNone(db_issue)
        self.assertEqual(req.creator_email, db_issue.creator_email)
        self.assertIsNone(db_issue.creator_name)
        self.assertEqual(req.issue.title, db_issue.title)
        self.assertEqual(req.issue.description, db_issue.description)
        self.assertIsNone(db_issue.rep_ids)

        mock_send_message.assert_called_once()

    def test_create_new_issue_validation_errors(self, mock_send_message):
        req = issue.CreateIssueRequest(
            creator_email='foo@foo.com' * 100,
            issue=issue.Issue(
                creator_name='Bob Smith' * 100,
                title='Issue Title' * 100,
                description='Issue description' * 10000,
                rep_ids=range(1000)))

        resp = self.service().invoke('create', req)
        self.assertEqual('REQUEST_ERROR', resp.response_code)
        self.assertIsNone(resp.issue)
        self.assertNumApiErrors(5, resp)
        self.assertHasApiError(resp, 'TOO_LONG', 'creator_email')
        self.assertHasApiError(resp, 'TOO_LONG', 'issue.creator_name')
        self.assertHasApiError(resp, 'TOO_LONG', 'issue.title')
        self.assertHasApiError(resp, 'TOO_LONG', 'issue.description')
        self.assertHasApiError(resp, 'TOO_LONG', 'issue.rep_ids')

        mock_send_message.assert_not_called()

    def test_create_new_issue_invalid_rep_ids(self, mock_send_message):
        req = issue.CreateIssueRequest(
            creator_email='foo@foo.com',
            issue=issue.Issue(
                creator_name='Bob Smith',
                title='Issue Title',
                description='Issue description',
                rep_ids=[888, 999]))

        resp = self.service().invoke('create', req)
        self.assertEqual('REQUEST_ERROR', resp.response_code)
        self.assertIsNone(resp.issue)
        self.assertNumApiErrors(2, resp)
        self.assertHasApiError(resp, 'INVALID_REP_ID', 'issue.rep_ids[0]')
        self.assertHasApiError(resp, 'INVALID_REP_ID', 'issue.rep_ids[1]')

        mock_send_message.assert_not_called()

    def test_create_new_issue_missing_required_fields(self, mock_send_message):
        req = issue.CreateIssueRequest(
            creator_email=None,
            issue=issue.Issue(
                title=None,
                description=None))

        json_resp = self.service().invoke_with_json('create', req.to_json())
        resp = issue.CreateIssueResponse.from_json(json_resp)
        self.assertEqual('REQUEST_ERROR', resp.response_code)
        self.assertIsNone(resp.issue)
        self.assertNumApiErrors(3, resp)
        self.assertHasApiError(resp, 'REQUIRED', 'creator_email')
        self.assertHasApiError(resp, 'REQUIRED', 'issue.title')
        self.assertHasApiError(resp, 'REQUIRED', 'issue.description')

        mock_send_message.assert_not_called()

    def test_get_existing_issue(self, mock_send_message):
        create_req = issue.CreateIssueRequest(
            creator_email='foo@foo.com',
            issue=issue.Issue(
                creator_name='Bob Smith',
                title='Issue Title',
                description='Issue description',
                rep_ids=[RD.nancy_pelosi.rep_id, RD.michael_enzi.rep_id]))

        create_resp = self.service().invoke('create', create_req)
        self.assertEqual('SUCCESS', create_resp.response_code)

        req = issue.GetIssueRequest(issue_id=create_resp.issue.issue_id)
        resp = self.service().invoke('get', req)
        self.assertEqual('SUCCESS', resp.response_code)
        self.assertIsNotNone(resp.issue)
        self.assertEqual(create_resp.issue.issue_id, resp.issue.issue_id)
        self.assertEqual(create_req.issue.creator_name, resp.issue.creator_name)
        self.assertEqual(create_req.issue.title, resp.issue.title)
        self.assertEqual(create_req.issue.description, resp.issue.description)
        self.assertEqual(create_req.issue.rep_ids, resp.issue.rep_ids)

    def test_get_invalid_issue_id(self, mock_send_message):
        req = issue.GetIssueRequest(issue_id=32283478234)
        resp = self.service().invoke('get', req)
        self.assertEqual('SUCCESS', resp.response_code)
        self.assertIsNone(resp.issue)

    def test_delete_issue(self, mock_send_message):
        create_req = issue.CreateIssueRequest(
            creator_email='foo@foo.com',
            issue=issue.Issue(
                creator_name='Bob Smith',
                title='Issue Title',
                description='Issue description',
                rep_ids=[RD.nancy_pelosi.rep_id, RD.michael_enzi.rep_id]))

        create_resp = self.service().invoke('create', create_req)
        self.assertEqual('SUCCESS', create_resp.response_code)

        req = issue.DeleteIssueRequest(
            token=issue_service._generate_issue_token(create_req.creator_email, create_resp.issue.issue_id),
            issue_id=create_resp.issue.issue_id)
        resp = self.service().invoke('delete', req)
        self.assertEqual('SUCCESS', resp.response_code)

        db_issue = I.query.get(create_resp.issue.issue_id)
        self.assertIsNone(db_issue)

    def test_delete_issue_invalid_token(self, mock_send_message):
        create_req = issue.CreateIssueRequest(
            creator_email='foo@foo.com',
            issue=issue.Issue(
                creator_name='Bob Smith',
                title='Issue Title',
                description='Issue description',
                rep_ids=[RD.nancy_pelosi.rep_id, RD.michael_enzi.rep_id]))

        create_resp = self.service().invoke('create', create_req)
        self.assertEqual('SUCCESS', create_resp.response_code)

        req = issue.DeleteIssueRequest(
            token='garbage',
            issue_id=create_resp.issue.issue_id)
        resp = self.service().invoke('delete', req)
        self.assertEqual('REQUEST_ERROR', resp.response_code)
        self.assertNumApiErrors(1, resp)
        self.assertHasApiError(resp, 'INVALID_TOKEN', 'token')

        db_issue = I.query.get(create_resp.issue.issue_id)
        self.assertIsNotNone(db_issue)

    def test_delete_issue_token_for_other_issue(self, mock_send_message):
        create_req = issue.CreateIssueRequest(
            creator_email='foo@foo.com',
            issue=issue.Issue(
                creator_name='Bob Smith',
                title='Issue Title',
                description='Issue description',
                rep_ids=[RD.nancy_pelosi.rep_id, RD.michael_enzi.rep_id]))

        create_resp = self.service().invoke('create', create_req)
        self.assertEqual('SUCCESS', create_resp.response_code)

        req = issue.DeleteIssueRequest(
            token=issue_service._generate_issue_token(create_req.creator_email, 9876),
            issue_id=create_resp.issue.issue_id)
        resp = self.service().invoke('delete', req)
        self.assertEqual('REQUEST_ERROR', resp.response_code)
        self.assertNumApiErrors(1, resp)
        self.assertHasApiError(resp, 'INVALID_TOKEN', 'token')

        db_issue = I.query.get(create_resp.issue.issue_id)
        self.assertIsNotNone(db_issue)

    def test_delete_issue_invalid_issue_id(self, mock_send_message):
        req = issue.DeleteIssueRequest(
            token=issue_service._generate_issue_token('bob@bob.com', 1234),
            issue_id=1234)
        resp = self.service().invoke('delete', req)
        self.assertEqual('REQUEST_ERROR', resp.response_code)
        self.assertNumApiErrors(1, resp)
        self.assertHasApiError(resp, 'UNKNOWN_ISSUE', 'issue_id')

    def test_update_issue_all_fields(self, mock_send_message):
        create_req = issue.CreateIssueRequest(
            creator_email='foo@foo.com',
            issue=issue.Issue(
                creator_name='Bob Smith',
                title='Issue Title',
                description='Issue description',
                rep_ids=[RD.nancy_pelosi.rep_id, RD.michael_enzi.rep_id]))
        create_resp = self.service().invoke('create', create_req)
        self.assertEqual('SUCCESS', create_resp.response_code)

        req = issue.UpdateIssueRequest(
            token=issue_service._generate_issue_token(create_req.creator_email, create_resp.issue.issue_id),
            issue=issue.Issue(
                issue_id=create_resp.issue.issue_id,
                creator_name='New Name',
                title='New Title',
                description='New Description',
                rep_ids=[RD.dianne_feinstein.rep_id]))
        resp = self.service().invoke('update', req)
        self.assertEqual('SUCCESS', resp.response_code)

        self.assertIsNotNone(resp.issue)
        self.assertEqual(create_resp.issue.issue_id, resp.issue.issue_id)
        self.assertEqual(req.issue.creator_name, resp.issue.creator_name)
        self.assertEqual(req.issue.title, resp.issue.title)
        self.assertEqual(req.issue.description, resp.issue.description)
        self.assertEqual(req.issue.rep_ids, resp.issue.rep_ids)

        db_issue = I.query.get(resp.issue.issue_id)
        self.assertIsNotNone(db_issue)
        self.assertEqual(create_req.creator_email, db_issue.creator_email)
        self.assertEqual(req.issue.creator_name, db_issue.creator_name)
        self.assertEqual(req.issue.title, db_issue.title)
        self.assertEqual(req.issue.description, db_issue.description)
        self.assertEqual(req.issue.rep_ids, db_issue.rep_ids)
        self.assertGreater(db_issue.time_updated, db_issue.time_created)

        mock_send_message.assert_called_once()

if __name__ == '__main__':
    unittest.main()
