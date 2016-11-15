from api import rep
from database import db_models

R = db_models.Rep

DB_CHAMBER_TO_API = {
    R.Chamber.HOUSE: rep.Rep.Chamber.HOUSE,
    R.Chamber.SENATE: rep.Rep.Chamber.SENATE,
}

DB_CHAMBER_TO_TITLE = {
    R.Chamber.HOUSE: 'Representative',
    R.Chamber.SENATE: 'Senator',
}

def db_rep_to_api(db_rep):
    if not db_rep:
        return None
    wash_dc_idx = db_rep.address_dc.find('Washington DC')
    address_dc_lines = [
        db_rep.address_dc[:wash_dc_idx - 1],
        db_rep.address_dc[wash_dc_idx:],
    ]
    return rep.Rep(
        first_name=db_rep.first_name,
        last_name=db_rep.last_name,
        state_code=db_rep.state_code,
        district_number=db_rep.district_number,
        district_code=db_rep.district_code,
        party_code=db_rep.party_code,
        chamber=DB_CHAMBER_TO_API.get(db_rep.chamber),
        title=DB_CHAMBER_TO_TITLE.get(db_rep.chamber),
        email_link=db_rep.email_link,
        email=db_rep.email,
        website=db_rep.website,
        address_dc=db_rep.address_dc,
        address_dc_lines=address_dc_lines,
        phone_dc=db_rep.phone_dc)

def db_reps_to_api(db_reps):
    if not db_reps:
        return None
    return [db_rep_to_api(db_rep) for db_rep in db_reps if db_rep]
