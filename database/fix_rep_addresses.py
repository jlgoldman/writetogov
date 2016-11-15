from database import db
from database import db_models

def main():
    for db_rep in db_models.Rep.query:
        db_rep.address_dc = db_rep.address_dc.replace('Washington DC', 'Washington DC,')
    db.session.commit()

if __name__ == '__main__':
    from tools import db_utils
    with db_utils.request_context():
        main()
