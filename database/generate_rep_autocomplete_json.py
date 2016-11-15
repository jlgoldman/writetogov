import json

from database import db_models
from logic import db_to_api
from util import fips

R = db_models.Rep

def ordinal(n):
    return '%d%s' % (n, 'tsnrhtdd'[(n / 10 % 10 != 1) * (n % 10 < 4) * n % 10::4])

def main():
    rep_datas = []
    for db_rep in R.query:
        district_ordinal = None
        if db_rep.chamber == R.Chamber.HOUSE:
            if db_rep.district_number > 0:
                district_ordinal = ordinal(db_rep.district_number)
            else:
                district_ordinal = 'At-Large'
        rep_datas.append([
            db_rep.first_name,
            db_rep.last_name,
            db_rep.state_code,
            fips.get_state_name_for_code(db_rep.state_code),
            db_rep.district_code,
            db_rep.district_number,
            district_ordinal,
            db_to_api.DB_CHAMBER_TO_TITLE.get(db_rep.chamber),
            ])
    print json.dumps(rep_datas)

if __name__ == '__main__':
    from tools import db_utils
    with db_utils.request_context():
        main()



