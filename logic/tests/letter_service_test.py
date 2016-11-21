import unittest

from PyPDF2 import PdfFileReader
import mock
import stripe

from api import letter
from logic import letter_service
from testing import test_base

class LetterServiceTest(test_base.RealDatabaseTest):
    def service(self):
        return letter_service.LetterServiceImpl()

    def test_generate_letter_pdf(self):
        req = letter.GenerateLetterRequest(
            rep_id=61,
            body='hello world',
            name_and_address='Bob Smith\nSan Francisco, CA')
        resp = self.service().invoke('generate', req)
        self.assertEqual('SUCCESS', resp.response_code)
        self.assertIsNotNone(resp.pdf_content)

    def test_generate_letter_pdf_with_address_page(self):
        req = letter.GenerateLetterRequest(
            rep_id=61,
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
            rep_id=61,
            body='hello world',
            name_and_address='Bob Smith\nSan Francisco, CA')
        mock_charge_create.return_value = None
        mock_make_lob_request.return_value = None
        resp = self.service().invoke('generate_and_mail', req)
        self.assertEqual('SUCCESS', resp.response_code)

        mock_charge_create.assert_called_once_with(
            amount=150,
            currency='usd',
            source='stripe-token',
            description='Mail a letter to Senator Mitch McConnell')
        pdf_reader = PdfFileReader(mock_make_lob_request.call_args[0][0])
        self.assertEqual(1, pdf_reader.getNumPages())

    @mock.patch('app.app.logger.error')
    @mock.patch.object(letter_service.LetterServiceImpl, '_make_lob_request')
    @mock.patch.object(stripe.Charge, 'create')
    def test_generate_and_mail_with_stripe_error(self, mock_charge_create, mock_make_lob_request, mock_log_error):
        req = letter.GenerateAndMailLetterRequest(
            stripe_token='stripe-token',
            rep_id=61,
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
            description='Mail a letter to Senator Mitch McConnell')
        mock_make_lob_request.assert_not_called()
        mock_log_error.assert_called_once()

if __name__ == '__main__':
    unittest.main()
