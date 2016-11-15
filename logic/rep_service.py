import apilib
from geoalchemy2.functions import ST_Contains
from geoalchemy2.types import Geometry
from sqlalchemy.sql.expression import cast

from api import rep
from database import db_models
from logic import db_to_api

R = db_models.Rep
D = db_models.District

HOUSE_SPEAKER_REP_ID = 530  # Paul Ryan
SENATE_MAJORITY_LEADER_REP_ID =  61 # Mitch McConnell


class RepServiceImpl(rep.RepService, apilib.ServiceImplementation):
    def __init__(self, **kwargs):
        pass

    def get(self, req):
        db_reps = R.query.filter(R.rep_id.in_(req.rep_ids)).all()
        return rep.GetRepsResponse(reps=db_to_api.db_reps_to_api(db_reps))

    def lookup(self, req):
        if req.district_code:
            house_rep = _get_house_rep_by_district_code(req.district_code)
            state_code = req.district_code[:2]
        else:
            house_rep = _get_house_rep_by_latlng(req.latlng)
            state_code = house_rep.state_code if house_rep else None

        senators = _get_senators_by_state_code(state_code)
        leadership = _get_leadership()

        return rep.LookupRepsResponse(
            house_rep=db_to_api.db_rep_to_api(house_rep),
            senators=db_to_api.db_reps_to_api(senators),
            leadership=db_to_api.db_reps_to_api(leadership))

    def process_unhandled_exception(self, exception):
        # For debugging
        return True

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
