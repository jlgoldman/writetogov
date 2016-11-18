import requests

from database import db_models

def main():
    for db_rep in db_models.Rep.query:
        if db_rep.photo_url:
            response = requests.get(db_rep.photo_url)
            outfile = open('data/rep_images/%d.jpg' % db_rep.rep_id, 'wb')
            outfile.write(response.content)
            outfile.close()

if __name__ == '__main__':
    from tools import db_utils
    with db_utils.request_context():
        main()
