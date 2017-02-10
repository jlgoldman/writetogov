import os
import requests

from database import db_models

def main():
    reps_by_id = {r.rep_id: r for r in db_models.Rep.query.all()}
    for fname in os.listdir('data/rep_images/'):
        if not fname.endswith('.jpg') or '-social' in fname:
            continue
        rep_id = int(fname.split('.')[0])
        if rep_id in reps_by_id:
            del reps_by_id[rep_id]
    for db_rep in reps_by_id.itervalues():
        if not db_rep.bioguide_id:
            print 'No bioguide id for %s %s (%s %s)' % (db_rep.first_name, db_rep.last_name, db_rep.state_code, db_rep.district_code)
            continue
        photo_url = 'http://bioguide.congress.gov/bioguide/photo/%s/%s.jpg' % (
            db_rep.bioguide_id[0], db_rep.bioguide_id)
        response = requests.get(photo_url)
        if response.status_code == 200:
            outfile = open('data/rep_images/%d.jpg' % db_rep.rep_id, 'wb')
            outfile.write(response.content)
            outfile.close()
            print 'Succcess for %s (%s %s)' % (db_rep.bioguide_id, db_rep.first_name, db_rep.last_name)
        else:
            print 'No image for %s (%s %s)' % (db_rep.bioguide_id, db_rep.first_name, db_rep.last_name)

if __name__ == '__main__':
    from tools import db_utils
    with db_utils.request_context():
        main()
