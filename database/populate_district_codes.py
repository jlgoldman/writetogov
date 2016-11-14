from database import db
from database import db_models
from util import fips

def main():
    for db_district in db_models.District.query.all():
        fips_info = fips.get_by_fips_code(db_district.statefp)
        db_district.state_name = fips_info.name
        db_district.state_code = fips_info.state_code
        db_district.district_code = '%s%s' % (fips_info.state_code, db_district.cd115fp)
    db.session.commit()

if __name__ == '__main__':
    from tools import db_utils
    with db_utils.request_context():
        main()
