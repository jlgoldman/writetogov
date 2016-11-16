import requests

from config import constants
from database import db
from database import db_models
from util import fips

R = db_models.Rep

HOUSE_MEMBERS_LEAVING_OFFICE_URL = 'https://api.propublica.org/congress/v1/114/house/members/leaving.json'
SENATE_MEMBERS_LEAVING_OFFICE_URL = 'https://api.propublica.org/congress/v1/114/senate/members/leaving.json'

PP_STATUS_TO_DB_STATUS = {
    'Retiring': R.Status.RETIRING,
    'Seeking another office': R.Status.SEEKING_OTHER_OFFICE,
    'Left Congress': R.Status.LEFT_CONGRESS,
    'Defeated in primary election': R.Status.DEFEATED_IN_PRIMARY,
}

def main():
    populate_senators()
    populate_reps()

def populate_senators():
    response = requests.get(SENATE_MEMBERS_LEAVING_OFFICE_URL, headers={'X-API-Key': constants.PROPUBLICA_API_KEY})
    for db_rep in R.query.filter(R.chamber == R.Chamber.SENATE):
        for member in response.json()['results'][0]['members']:
            if db_rep.state_code == member['state'] and db_rep.last_name == member['last_name']:
                db_rep.status = PP_STATUS_TO_DB_STATUS[member['status']]
                db_rep.status_note = member['note']
                break
    db.session.commit()

def populate_reps():
    response = requests.get(HOUSE_MEMBERS_LEAVING_OFFICE_URL, headers={'X-API-Key': constants.PROPUBLICA_API_KEY})
    info_by_district_code = {}
    for member in response.json()['results'][0]['members']:
        if member['state'] in fips.ONE_DISTRICT_STATE_CODES:
            district_code = '%s00' % member['state']
        else:
            district_code = '%s%02d' % (member['state'], int(member['district']))
        info_by_district_code[district_code] = {
            'status': member['status'],
            'note': member['note'],
        }
    for db_rep in R.query.filter(R.district_code.in_(info_by_district_code.keys())):
        info = info_by_district_code[db_rep.district_code]
        db_rep.status = PP_STATUS_TO_DB_STATUS[info['status']]
        db_rep.status_note = info['note']
    db.session.commit()

if __name__ == '__main__':
    from tools import db_utils
    with db_utils.request_context():
        main()
