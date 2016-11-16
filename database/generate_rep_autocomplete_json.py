import json

from database import db_models
from logic import db_to_api

R = db_models.Rep

def main():
    rep_datas = []
    for db_rep in R.query:
        rep_datas.append([
            db_rep.rep_id,
            db_rep.first_name,
            db_rep.last_name,
            db_rep.state_code,
            db_rep.state_name(),
            db_rep.district_code,
            db_rep.district_number,
            db_rep.district_ordinal(),
            db_to_api.DB_CHAMBER_TO_TITLE.get(db_rep.chamber),
            ])
    print json.dumps(rep_datas)

if __name__ == '__main__':
    from tools import db_utils
    with db_utils.request_context():
        main()
