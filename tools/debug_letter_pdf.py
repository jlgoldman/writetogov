import random

from api import letter
from logic import letter_service

def main():
    req = letter.GenerateLetterRequest(
        rep_id=61,
        body='hello world',
        closing='Bob Smith\nSan Francisco, CA')
    service = letter_service.LetterServiceImpl()
    resp = service.invoke('generate', req)
    output_filename = 'debug-letter-%d.pdf' % random.uniform(1, 1000000)
    output_file = open(output_filename, 'wb')
    output_file.write(resp.pdf_content)
    output_file.close()
    print 'Wrote %s' % output_filename

if __name__ == '__main__':
    from tools import db_utils
    with db_utils.request_context():
        main()
