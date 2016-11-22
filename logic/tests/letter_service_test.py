import logging
import unittest

import lob
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

# Silence logging that's not helpful for tests
logging.getLogger('apilib.service').addHandler(logging.NullHandler())

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

    @mock.patch.object(lob.Letter, 'create')
    @mock.patch.object(lob.Address, 'create')
    @mock.patch.object(stripe.Charge, 'create')
    def test_generate_and_mail_success(self, mock_charge_create, mock_address_create, mock_letter_create):
        req = letter.GenerateAndMailLetterRequest(
            stripe_token='stripe-token',
            email='foo@foo.com',
            rep_id=pelosi.rep_id,
            body='hello world',
            name_and_address='Bob Smith\r\n123 Main St\r\nSan Francisco, CA 94103')

        mock_address_create.return_value = {'id': 'lob-address-id'}
        mock_charge_create.return_value = stripe.Charge(id='stripe-charge-id')
        mock_letter_create.return_value = {
            'id': 'lob-letter-id',
            'url': 'lob-url',
            'expected_delivery_date': '2016-11-12',
            }

        resp = self.service().invoke('generate_and_mail', req)
        self.assertEqual('SUCCESS', resp.response_code)
        self.assertEqual('November 12', resp.expected_delivery_date)
        self.assertEqual('lob-url', resp.lob_pdf_url)

        mock_charge_create.assert_called_once_with(
            amount=150,
            currency='usd',
            source='stripe-token',
            description='Letter to Representative Nancy Pelosi')

        mock_letter_create.assert_called_once()
        letter_kwargs = mock_letter_create.call_args[1]
        self.assertEqual('Letter to Representative Nancy Pelosi', letter_kwargs['description'])
        self.assertTrue(letter_kwargs['double_sided'])
        self.assertFalse(letter_kwargs['color'])
        self.assertEqual('insert_blank_page', letter_kwargs['address_placement'])
        pdf_reader = PdfFileReader(letter_kwargs['file'])
        self.assertEqual(1, pdf_reader.getNumPages())
        self.assertEqual('lob-address-id', letter_kwargs['from_address'])
        expected_to_address = {
            'name': u'Representative Nancy Pelosi',
            'address_line1': u'233 Longworth House Office Building',
            'address_city': 'Washington',
            'address_state': 'DC',
            'address_country': 'US',
            'address_zip': u'20515',
            }
        self.assertDictEqual(expected_to_address, letter_kwargs['to_address'])

        mock_address_create.assert_called_once_with(
            name='Bob Smith',
            address_line1='123 Main St',
            address_city='San Francisco',
            address_state='CA',
            address_zip='94103',
            address_country='US')

        db_rm = RM.query.filter(RM.email == req.email).first()
        self.assertIsNotNone(db_rm)
        self.assertEqual('stripe-charge-id', db_rm.stripe_charge_id)
        self.assertEqual(req.rep_id, db_rm.rep_id)
        self.assertEqual('lob-letter-id', db_rm.lob_letter_id)
        self.assertIsNotNone(db_rm.time_created)
        self.assertIsNotNone(db_rm.time_updated)
        self.assertGreater(db_rm.time_updated, db_rm.time_created)

    @mock.patch('app.app.logger.error')
    @mock.patch.object(lob.Letter, 'create')
    @mock.patch.object(lob.Address, 'create')
    @mock.patch.object(stripe.Charge, 'create')
    def test_generate_and_mail_with_stripe_error(self, mock_charge_create, mock_address_create,
            mock_letter_create, mock_log_error):
        req = letter.GenerateAndMailLetterRequest(
            stripe_token='stripe-token',
            email='foo@foo.com',
            rep_id=pelosi.rep_id,
            body='hello world',
            name_and_address='Bob Smith\nSan Francisco, CA')

        mock_address_create.return_value = {'id': 'lob-address-id'}
        mock_charge_create.side_effect = stripe.error.CardError(
            message='error message', param=None, code=None)
        mock_letter_create.return_value = None

        resp = self.service().invoke('generate_and_mail', req)
        self.assertEqual('REQUEST_ERROR', resp.response_code)
        self.assertEqual(1, len(resp.errors))
        self.assertEqual('There was an error charging your card: error message', resp.errors[0].message)

        mock_charge_create.assert_called_once_with(
            amount=150,
            currency='usd',
            source='stripe-token',
            description='Letter to Representative Nancy Pelosi')
        mock_address_create.assert_called_once()
        mock_letter_create.assert_not_called()
        mock_log_error.assert_called_once()

        db_rm = RM.query.filter(RM.email == req.email).first()
        self.assertIsNone(db_rm)

    @mock.patch('app.app.logger.error')
    @mock.patch.object(lob.Letter, 'create')
    @mock.patch.object(lob.Address, 'create')
    @mock.patch.object(stripe.Charge, 'create')
    def test_generate_and_mail_with_lob_address_error(self, mock_charge_create, mock_address_create,
            mock_letter_create, mock_log_error):
        req = letter.GenerateAndMailLetterRequest(
            stripe_token='stripe-token',
            email='foo@foo.com',
            rep_id=pelosi.rep_id,
            body='hello world',
            name_and_address='Bob Smith\nSan Francisco, CA')

        mock_address_create.side_effect = lob.error.InvalidRequestError('address_line1 is required')
        mock_charge_create.return_value = None
        mock_letter_create.return_value = None

        resp = self.service().invoke('generate_and_mail', req)
        self.assertEqual('REQUEST_ERROR', resp.response_code)
        self.assertEqual(1, len(resp.errors))
        self.assertEqual(
            'There was an error with your address: line1 is required',
            resp.errors[0].message)

        mock_address_create.assert_called_once()
        mock_charge_create.assert_not_called()
        mock_letter_create.assert_not_called()
        mock_log_error.assert_called_once()

        db_rm = RM.query.filter(RM.email == req.email).first()
        self.assertIsNone(db_rm)

    @mock.patch('app.app.logger.error')
    @mock.patch.object(lob.Letter, 'create')
    @mock.patch.object(lob.Address, 'create')
    @mock.patch.object(stripe.Charge, 'create')
    def test_generate_and_mail_with_lob_mail_error(self, mock_charge_create, mock_address_create,
            mock_letter_create, mock_log_error):
        req = letter.GenerateAndMailLetterRequest(
            stripe_token='stripe-token',
            email='foo@foo.com',
            rep_id=pelosi.rep_id,
            body='hello world',
            name_and_address='Bob Smith\nSan Francisco, CA')

        mock_address_create.return_value = {'id': 'lob-address-id'}
        mock_charge_create.return_value = stripe.Charge(id='stripe-charge-id')
        mock_letter_create.side_effect = lob.error.LobError('test error')

        resp = self.service().invoke('generate_and_mail', req)
        self.assertEqual('SERVER_ERROR', resp.response_code)
        self.assertEqual(1, len(resp.errors))
        self.assertEqual(
            'There was an error submitting your letter to be mailed. Please contact info@writetogov.com.',
            resp.errors[0].message)

        mock_address_create.assert_called_once()
        mock_charge_create.assert_called_once()
        mock_letter_create.assert_called_once()
        mock_log_error.assert_called_once()

        db_rm = RM.query.filter(RM.email == req.email).first()
        self.assertIsNotNone(db_rm)
        self.assertEqual('stripe-charge-id', db_rm.stripe_charge_id)
        self.assertEqual(req.rep_id, db_rm.rep_id)
        self.assertIsNone(db_rm.lob_letter_id)
        self.assertIsNotNone(db_rm.time_created)
        self.assertIsNotNone(db_rm.time_updated)
        self.assertEqual(db_rm.time_updated, db_rm.time_created)

    def test_parse_address_request(self):
        req = letter.ParseAddressRequest(
            name_and_address='Bob Smith\n123 Main St\nSan Francisco, CA 94103')
        resp = self.service().invoke('parse_address', req)
        self.assertEqual('SUCCESS', resp.response_code)
        self.assertEqual('Bob Smith', resp.name)
        self.assertEqual('123 Main St', resp.line1)
        self.assertEqual('San Francisco', resp.city)
        self.assertEqual('CA', resp.state)
        self.assertEqual('94103', resp.zip)

    def test_newlines_converted_to_br(self):
        req = letter.GenerateLetterRequest(
            rep_id=pelosi.rep_id,
            body='hello\nworld',
            name_and_address='Bob Smith\nSan Francisco, CA')
        html = self.service()._generate_html(req)
        self.assertTrue('hello<br/>world' in html)
        self.assertTrue('Bob Smith<br/>San Francisco, CA' in html)

        req = letter.GenerateLetterRequest(
            rep_id=pelosi.rep_id,
            body='hello\r\nworld',
            name_and_address='Bob Smith\r\nSan Francisco, CA')
        html = self.service()._generate_html(req)
        self.assertTrue('hello<br/>world' in html)
        self.assertTrue('Bob Smith<br/>San Francisco, CA' in html)

class SenderAddressParsingTest(unittest.TestCase):
    def parse(self, lines):
        addr_string = '\n'.join(lines)
        return letter_service._sender_name_and_address_to_lob_address(addr_string)

    def test_basic_addr(self):
        lob_addr = self.parse([
            'Bob Smith',
            '123 Main',
            'Frankfort, KY 12345',
            ])
        self.assertEqual('Bob Smith', lob_addr['name'])
        self.assertEqual('123 Main', lob_addr['address_line1'])
        self.assertEqual('Frankfort', lob_addr['address_city'])
        self.assertEqual('KY', lob_addr['address_state'])
        self.assertEqual('12345', lob_addr['address_zip'])
        self.assertEqual('US', lob_addr['address_country'])

    def test_zip4(self):
        lob_addr = self.parse([
            'Bob Smith',
            '123 Main',
            'Frankfort, KY 12345-9876',
            ])
        self.assertEqual('Bob Smith', lob_addr['name'])
        self.assertEqual('123 Main', lob_addr['address_line1'])
        self.assertEqual('Frankfort', lob_addr['address_city'])
        self.assertEqual('KY', lob_addr['address_state'])
        self.assertEqual('12345-9876', lob_addr['address_zip'])
        self.assertEqual('US', lob_addr['address_country'])

        lob_addr = self.parse([
            'Bob Smith',
            '123 Main',
            'Frankfort, KY 12345 - 9876',
            ])
        self.assertEqual('12345-9876', lob_addr['address_zip'])

    def test_long_state_name(self):
        lob_addr = self.parse([
            'Bob Smith',
            '123 Main',
            'Frankfort, kentucky 12345',
            ])
        self.assertEqual('Bob Smith', lob_addr['name'])
        self.assertEqual('123 Main', lob_addr['address_line1'])
        self.assertEqual('Frankfort', lob_addr['address_city'])
        self.assertEqual('KY', lob_addr['address_state'])
        self.assertEqual('12345', lob_addr['address_zip'])
        self.assertEqual('US', lob_addr['address_country'])

if __name__ == '__main__':
    unittest.main()
