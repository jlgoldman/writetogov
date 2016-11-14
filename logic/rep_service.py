import apilib
from geoalchemy2.functions import ST_Contains
from geoalchemy2.types import Geometry
from sqlalchemy.sql.expression import cast

from api import rep
from database import db_models

R = db_models.Rep
D = db_models.District

HOUSE_SPEAKER_REP_ID = 530  # Paul Ryan
SENATE_MAJORITY_LEADER_REP_ID =  61 # Mitch McConnell

DB_CHAMBER_TO_API = {
    R.Chamber.HOUSE: rep.Rep.Chamber.HOUSE,
    R.Chamber.SENATE: rep.Rep.Chamber.SENATE,
}

class RepServiceImpl(rep.RepService, apilib.ServiceImplementation):
    def __init__(self, **kwargs):
        pass

    def get(self, req):
        if req.district_code:
            house_rep = _get_house_rep_by_district_code(req.district_code)
            state_code = req.district_code[:2]
        else:
            house_rep = _get_house_rep_by_latlng(req.latlng)
            state_code = house_rep.state_code if house_rep else None

        senators = _get_senators_by_state_code(state_code)
        leadership = _get_leadership()

        return rep.GetRepsResponse(
            house_rep=db_rep_to_api(house_rep),
            senators=db_reps_to_api(senators),
            leadership=db_reps_to_api(leadership))

    def process_unhandled_exception(self, exception):
        # For debugging
        return True

def db_rep_to_api(db_rep):
    if not db_rep:
        return None
    return rep.Rep(
        first_name=db_rep.first_name,
        last_name=db_rep.last_name,
        state_code=db_rep.state_code,
        district_number=db_rep.district_number,
        district_code=db_rep.district_code,
        party_code=db_rep.party_code,
        chamber=DB_CHAMBER_TO_API.get(db_rep.chamber),
        email_link=db_rep.email_link,
        email=db_rep.email,
        website=db_rep.website,
        address_dc=db_rep.address_dc,
        phone_dc=db_rep.phone_dc)

def db_reps_to_api(db_reps):
    if not db_reps:
        return None
    return [db_rep_to_api(db_rep) for db_rep in db_reps if db_rep]

def _get_house_rep_by_district_code(code):
    if not code:
        return None
    return R.query \
        .filter(R.district_code == code.upper()) \
        .first()

def _get_senators_by_state_code(code):
    if not code:
        return None
    return R.query \
        .filter(R.chamber == R.Chamber.SENATE) \
        .filter(R.state_code == code.upper()) \
        .all()

def _get_house_rep_by_latlng(api_latlng):
    # SELECT district_code FROM district WHERE ST_CONTAINS(geog::geometry, ST_GeomFromText('POINT(lng lat)', 4326));
    point = 'SRID=%d; POINT(%s %s)' % (db_models.SRID, api_latlng.lng, api_latlng.lat)
    db_district = D.query \
        .filter(ST_Contains(
            cast(D.geog, Geometry()),
            point)) \
        .first()
    if db_district:
        return _get_house_rep_by_district_code(db_district.district_code)
    return None

def _get_leadership():
    return R.query \
        .filter(R.rep_id.in_([HOUSE_SPEAKER_REP_ID, SENATE_MAJORITY_LEADER_REP_ID])) \
        .all()
