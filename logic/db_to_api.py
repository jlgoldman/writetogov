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

DB_STATUS_TO_API = {
    R.Status.ACTIVE: rep.Rep.Status.ACTIVE,
    R.Status.LEFT_CONGRESS: rep.Rep.Status.LEFT_CONGRESS,
    R.Status.DEFEATED_IN_GENERAL: rep.Rep.Status.DEFEATED_IN_GENERAL,
    R.Status.DEFEATED_IN_PRIMARY: rep.Rep.Status.DEFEATED_IN_PRIMARY,
    R.Status.RETIRING: rep.Rep.Status.RETIRING,
    R.Status.SEEKING_OTHER_OFFICE: rep.Rep.Status.SEEKING_OTHER_OFFICE,
    R.Status.PENDING_RESULT: rep.Rep.Status.PENDING_RESULT,
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
        rep_id=db_rep.rep_id,
        first_name=db_rep.first_name,
        last_name=db_rep.last_name,
        state_code=db_rep.state_code,
        state_name=db_rep.state_name(),
        district_number=db_rep.district_number,
        district_code=db_rep.district_code,
        district_ordinal=db_rep.district_ordinal(),
        party_code=db_rep.party_code,
        chamber=DB_CHAMBER_TO_API.get(db_rep.chamber),
        title=DB_CHAMBER_TO_TITLE.get(db_rep.chamber),
        email_link=db_rep.email_link,
        email=db_rep.email,
        website=db_rep.website,
        address_dc=db_rep.address_dc,
        address_dc_lines=address_dc_lines,
        phone_dc=db_rep.phone_dc,
        status=DB_STATUS_TO_API.get(db_rep.status),
        status_note=db_rep.status_note,
        photo_url=db_rep.photo_url)

def db_reps_to_api(db_reps):
    if not db_reps:
        return None
    return [db_rep_to_api(db_rep) for db_rep in db_reps if db_rep]
