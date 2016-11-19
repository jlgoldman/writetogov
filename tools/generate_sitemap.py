from database import db_models

def main():
    district_codes = set()
    rep_ids = set()
    for db_rep in db_models.Rep.query:
        if db_rep.district_code:
            district_codes.add(db_rep.district_code)
        rep_ids.add(db_rep.rep_id)
    print 'https://www.writetogov.com/'
    for district_code in sorted(district_codes):
        print 'https://www.writetogov.com/district/%s' % district_code
    for rep_id in sorted(rep_ids):
        print 'https://www.writetogov.com/compose/%d' % rep_id

if __name__ == '__main__':
    from tools import db_utils
    with db_utils.request_context():
        main()
