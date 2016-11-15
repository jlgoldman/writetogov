import requests

from database import db
from database import db_models

R = db_models.Rep

def main():
    for db_rep in R.query:
        if db_rep.bioguide_id:
            photo_url = 'http://bioguide.congress.gov/bioguide/photo/%s/%s.jpg' % (
                db_rep.bioguide_id[0], db_rep.bioguide_id)
            resp = requests.get(photo_url)
            if resp.status_code == 200:
                db_rep.photo_url = photo_url
    db.session.commit()

if __name__ == '__main__':
    from tools import db_utils
    with db_utils.request_context():
        main()



