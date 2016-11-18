import re

import requests

from database import db_models

R = db_models.Rep

REPS_WITHOUT_IMAGES = {
    'AZ02': 'Martha McSally',
    'CA11': 'Mark DeSaulnier',
    'CA25': 'Stephen Knight',
    'CA35': 'Norma Torres',
    'CA37': 'Karen Bass',
    'DE00': 'John Carney',
    'FL13': 'David Jolly',
    'FL19': 'Curt Clawson',
    'CO04': 'Ken Buck',
    'FL26': 'Carlos Curbelo',
    'GA01': 'Earl Carter',
    'IL18': 'Darin LaHood',
    'GA11': 'Barry Loudermilk',
    'IA01': 'Rod Blum',
    'IA03': 'David Young',
    'IL12': 'Mike Bost',
    'IN04': 'Todd Rokita',
    'IN08': 'Larry Bucshon',
    'KS03': 'Kevin Yoder',
    'MS01': 'Trent Kelly',
    'LA06': 'Garret Graves',
    'ME02': 'Bruce Poliquin',
    'MI08': 'Mike Bishop',
    'MI11': 'David Trott',
    'MI12': 'Debbie Dingell',
    'MI14': 'Brenda Lawrence',
    'MN06': 'Tom Emmer',
    'NY11': 'Daniel Donovan',
    'MT00': 'Ryan Zinke',
    'NC06': 'Mark Walker',
    'NC07': 'David Rouzer',
    'NC12': 'Alma Adams',
    'NV04': 'Cresent Hardy',
    'NY01': 'Lee Zeldin',
    'OH08': 'Warren Davidson',
    'NY21': 'Elise Stefanik',
    'NY24': 'John Katko',
    'OH15': 'Steve Stivers',
    'OR01': 'Suzanne Bonamici',
    'PA06': 'Ryan Costello',
    'PA13': 'Brendan Boyle',
    'RI01': 'David Cicilline',
    'TN06': 'Diane Black',
    'TX04': 'John Ratcliffe',
    'TX23': 'Will Hurd',
    'UT04': 'Mia Love',
    'VA07': 'Dave Brat',
    'VA10': 'Barbara Comstock',
    'NY04': 'Kathleen Rice',
    'VI00': 'Stacey Plaskett',
    'WV03': 'Evan Jenkins',
}

IMG_RE = re.compile('<img\s+alt="([^"]+)"\s+src="([^"]+)"')

def main():
    for district_code, rep_name in REPS_WITHOUT_IMAGES.iteritems():
        url = 'https://en.wikipedia.org/wiki/%s' % rep_name.replace(' ', '_')
        try:
            db_rep = R.query.filter(R.district_code == district_code).one()
            response = requests.get(url)
            matches = IMG_RE.findall(response.text)
            photo_url = None
            for alt_text, photo_url_candidate in matches:
                alt_text = alt_text.lower()
                if ((rep_name.split()[0].lower() in alt_text
                    and rep_name.split()[1].lower() in alt_text)
                    or '220px' in photo_url_candidate):
                    photo_url = photo_url_candidate
                    if not photo_url.startswith('http'):
                        photo_url = 'https:' + photo_url
            if photo_url:
                print photo_url
                photo_response = requests.get(photo_url)
                outfile = open('data/tmp/%d.jpg' % db_rep.rep_id, 'wb')
                outfile.write(photo_response.content)
                outfile.close()
            else:
                print 'No rep image found for %d - %s (%s) on page %s' % (
                    db_rep.rep_id, district_code, rep_name, url)

        except Exception as e:
            print 'Error getting rep image for %s (%s): %s' % (
                district_code, rep_name, e)

if __name__ == '__main__':
    from tools import db_utils
    with db_utils.request_context():
        main()
