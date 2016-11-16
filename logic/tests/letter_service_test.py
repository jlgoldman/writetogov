import unittest

from api import letter
from logic import letter_service
from testing import test_base

class RepServiceTest(test_base.RealDatabaseTest):
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


if __name__ == '__main__':
    unittest.main()
