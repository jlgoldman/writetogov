from lxml import etree
import requests

from database import db
from database import db_models

def main():
    populate_senators()
    populate_house_reps()
    db.session.commit()

def populate_senators():
    resp = requests.get('http://www.senate.gov/general/contact_information/senators_cfm.xml')
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
            bioguide_id=get_field(member, 'bioguide_id'))
        db.session.add(db_rep)

def populate_house_reps():
    resp = requests.get('http://clerk.house.gov/xml/lists/MemberData.xml')
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
            bioguide_id=get_field(member_info, 'bioguideID'))
        db.session.add(db_rep)

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
