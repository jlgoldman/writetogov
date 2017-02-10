from lxml import etree
import requests

from database import db
from database import db_models

USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
HEADERS = {'User-Agent': USER_AGENT}

def main():
    populate_senators()
    populate_house_reps()
    db.session.commit()

def populate_senators():
    resp = requests.get('http://www.senate.gov/general/contact_information/senators_cfm.xml', headers=HEADERS)
    root = etree.fromstring(resp.content)
    for member in root.xpath('//member'):
        db_rep = db_models.Rep(
            first_name=get_field(member, 'first_name'),
            last_name=get_field(member, 'last_name'),
            state_code=get_field(member, 'state'),
            district_number=None,
            district_code=None,
            party_code=get_field(member, 'party'),
            chamber=db_models.Rep.Chamber.SENATE,
            email_link=get_field(member, 'email'),
            website=get_field(member, 'website'),
            address_dc=get_field(member, 'address'),
            phone_dc=get_field(member, 'phone'),
            bioguide_id=get_field(member, 'bioguide_id'),
            status=db_models.Rep.Status.ACTIVE)
        existing_db_rep = db_models.Rep.query.filter(db_models.Rep.bioguide_id == db_rep.bioguide_id).first()
        if not existing_db_rep:
            rep_to_delete = db_models.Rep.query \
                .filter(db_models.Rep.state_code == db_rep.state_code) \
                .filter(db_models.Rep.chamber == db_models.Rep.Chamber.SENATE) \
                .filter(db_models.Rep.status != db_models.Rep.Status.ACTIVE) \
                .first()
            if rep_to_delete:
                db.session.delete(rep_to_delete)
                print 'Deleting senator (%s) with status "%s": %s %s' % (rep_to_delete.state_code, rep_to_delete.status,
                    rep_to_delete.first_name, rep_to_delete.last_name)
            print 'Adding new senator (%s): %s %s' % (db_rep.state_code, db_rep.first_name, db_rep.last_name)
            db.session.add(db_rep)

def populate_house_reps():
    resp = requests.get('http://clerk.house.gov/xml/lists/MemberData.xml', headers=HEADERS)
    root = etree.fromstring(resp.content)
    for member in root.xpath('//members/member'):
        member_info = member.xpath('./member-info')[0]
        district_code = get_field(member, 'statedistrict')
        address = address_from_member_info(member_info)
        db_rep = db_models.Rep(
            first_name=get_field(member_info, 'firstname'),
            last_name=get_field(member_info, 'lastname'),
            state_code=member_info.xpath('./state/@postal-code')[0],
            district_number=int(district_code[2:]),
            district_code=district_code,
            party_code=get_field(member_info, 'party'),
            chamber=db_models.Rep.Chamber.HOUSE,
            email_link=None,
            website=None,
            address_dc=address,
            phone_dc=get_field(member_info, 'phone'),
            bioguide_id=get_field(member_info, 'bioguideID'),
            status=db_models.Rep.Status.ACTIVE)
        existing_db_rep = db_models.Rep.query.filter(db_models.Rep.bioguide_id == db_rep.bioguide_id).first()
        if not existing_db_rep:
            rep_to_delete = db_models.Rep.query.filter(db_models.Rep.district_code == district_code).one()
            db.session.delete(rep_to_delete)
            db.session.add(db_rep)
            print 'Deleting representative (%s) with status "%s": %s %s' % (rep_to_delete.district_code, rep_to_delete.status,
                rep_to_delete.first_name, rep_to_delete.last_name)
            print 'Adding new representative (%s): %s %s' % (db_rep.district_code, db_rep.first_name, db_rep.last_name)

def get_field(elem, field_name):
    value = elem.xpath('./%s' % field_name)[0].text
    return value.strip() if value else None

HOUSE_OFFICE_CODE_TO_NAME = {
    'LHOB': 'Cannon House Office Building',
    'CHOB': 'Longworth House Office Building',
    'RHOB': 'Rayburn House Office Building',
}

def address_from_member_info(member_info):
    building_code = get_field(member_info, 'office-building')
    building_name = HOUSE_OFFICE_CODE_TO_NAME.get(building_code)
    if not building_name:
        raise Exception('Unknown House office building for rep %s %s: %s' % (
            get_field(member_info('firstname'), get_field(member_info, 'lastname'), building_code)))
    office_room = get_field(member_info, 'office-room')
    office_zip = get_field(member_info, 'office-zip')
    return '%s %s Washington DC %s' % (office_room, building_name, office_zip)

if __name__ == '__main__':
    from tools import db_utils
    with db_utils.request_context():
        main()
