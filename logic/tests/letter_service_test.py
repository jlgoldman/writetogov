import unittest

import mock
from PyPDF2 import PdfFileReader
import stripe

from api import letter
from database import db_models
from logic import letter_service
from testing import test_base
from testing import test_data

pelosi = test_data.RepData.nancy_pelosi
RM = db_models.RepMailing

class LetterServiceTest(test_base.DatabaseWithTestdataTest):
    def service(self):
        return letter_service.LetterServiceImpl()

    def test_generate_letter_pdf(self):
        req = letter.GenerateLetterRequest(
            rep_id=pelosi.rep_id,
            body='hello world',
            name_and_address='Bob Smith\nSan Francisco, CA')
        resp = self.service().invoke('generate', req)
        self.assertEqual('SUCCESS', resp.response_code)
        self.assertIsNotNone(resp.pdf_content)

    def test_generate_letter_pdf_with_address_page(self):
        req = letter.GenerateLetterRequest(
            rep_id=pelosi.rep_id,
            body='hello world',
            name_and_address='Bob Smith\nSan Francisco, CA',
            include_address_page=True)
        resp = self.service().invoke('generate', req)
        self.assertEqual('SUCCESS', resp.response_code)
        self.assertIsNotNone(resp.pdf_content)

    @mock.patch.object(letter_service.LetterServiceImpl, '_make_lob_request')
    @mock.patch.object(stripe.Charge, 'create')
    def test_generate_and_mail_success(self, mock_charge_create, mock_make_lob_request):
        req = letter.GenerateAndMailLetterRequest(
            stripe_token='stripe-token',
            email='foo@foo.com',
            rep_id=pelosi.rep_id,
            body='hello world',
            name_and_address='Bob Smith\nSan Francisco, CA')
        mock_charge_create.return_value = stripe.Charge(id='stripe-charge-id')
        mock_make_lob_request.return_value = None
        resp = self.service().invoke('generate_and_mail', req)
        self.assertEqual('SUCCESS', resp.response_code)

        mock_charge_create.assert_called_once_with(
            amount=150,
            currency='usd',
            source='stripe-token',
            description='Mail a letter to Representative Nancy Pelosi')
        pdf_reader = PdfFileReader(mock_make_lob_request.call_args[0][0])
        self.assertEqual(1, pdf_reader.getNumPages())

        db_rm = RM.query.filter(RM.email == req.email).first()
        self.assertIsNotNone(db_rm)
        self.assertEqual('stripe-charge-id', db_rm.stripe_charge_id)
        self.assertEqual(req.rep_id, db_rm.rep_id)
        self.assertIsNotNone(db_rm.time_created)
        self.assertIsNotNone(db_rm.time_updated)

    @mock.patch('app.app.logger.error')
    @mock.patch.object(letter_service.LetterServiceImpl, '_make_lob_request')
    @mock.patch.object(stripe.Charge, 'create')
    def test_generate_and_mail_with_stripe_error(self, mock_charge_create, mock_make_lob_request, mock_log_error):
        req = letter.GenerateAndMailLetterRequest(
            stripe_token='stripe-token',
            email='foo@foo.com',
            rep_id=pelosi.rep_id,
            body='hello world',
            name_and_address='Bob Smith\nSan Francisco, CA')
        mock_charge_create.side_effect = stripe.error.CardError(
            message='error message', param=None, code=None)
        mock_make_lob_request.return_value = None
        resp = self.service().invoke('generate_and_mail', req)
        self.assertEqual('REQUEST_ERROR', resp.response_code)
        self.assertEqual(1, len(resp.errors))
        self.assertEqual('There was an error charging your card: error message', resp.errors[0].message)

        mock_charge_create.assert_called_once_with(
            amount=150,
            currency='usd',
            source='stripe-token',
            description='Mail a letter to Representative Nancy Pelosi')
        mock_make_lob_request.assert_not_called()
        mock_log_error.assert_called_once()

        db_rm = RM.query.filter(RM.email == req.email).first()
        self.assertIsNone(db_rm)


if __name__ == '__main__':
    unittest.main()
