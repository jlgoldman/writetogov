import json

from database import db
from database import db_models

DATA_FNAME = 'data/nyt_house_results.20161115.json'

R = db_models.Rep

def main():
    reps_by_district_code = {r.district_code: r for r in R.query}
    races = json.load(open(DATA_FNAME))
    for race in races:
        seat_number = 0 if race['seat_name'] == 'At-Large' else race['seat']
        district_code = '%s%02d' % (race['state_id'], seat_number)
        if race['result'] == 'winner':
            winner = next(c for c in race['candidates'] if c.get('winner'))
            db_rep = reps_by_district_code[district_code]
            if district_code in ('FL21', 'FL22', 'CA01', 'CA29', 'CA38', 'IL04', 'NJ10', 'NM03', 'NY07'):
                # These are cases where the official spellings of names conflict with the nytimes
                # spellings and look like mismatches, like NM03 Lujan,
                # or the case of FL21 and FL22 which were redistricted to each other
                # but the incumbents of the old districts won the new ones.
                db_rep.status = R.Status.ACTIVE
            else:
                if race['has_incumbent']:
                    if winner['last_name'] == db_rep.last_name:
                        db_rep.status = R.Status.ACTIVE
                    else:
                        db_rep.status = R.Status.DEFEATED
                else:
                    db_rep.status = R.Status.RETIRING
    db.session.commit()

if __name__ == '__main__':
    from tools import db_utils
    with db_utils.request_context():
        main()



