from geoalchemy2 import Geography
from sqlalchemy.dialects import postgresql

from database import db
from util import fips
from util import text

SRID = 4326

# This table is auto-generated by shp2sql based on the TIGER shapefile
# tl_2016_us_cd115.zip (https://www.census.gov/cgi-bin/geo/shapefiles/index.php?year=2016&layergroup=Congressional+Districts+%28115%29).
# We then augment it with additional columns for state
# name and code, since by default it only includes FIPS codes.
#
# Table creation was initiated using:
# shp2pgsql -G -s 4269:4326 tl_2016_us_cd115.shp district > district_raw.sql
#
# Table altered using:
# ALTER TABLE district
#   ADD COLUMN state_name character varying(50),
#   ADD COLUMN state_code character varying(2),
#   ADD COLUMN district_code character varying(4);
# CREATE INDEX idx_district_state_code ON district USING btree (state_code);
# CREATE INDEX idx_district_district_code ON district USING btree (district_code);
#
# Then extra columns are popualted using database/populate_district_codes.py
class District(db.Model):
    gid = db.Column(db.Integer, primary_key=True)
    statefp = db.Column(db.String(2), index=True)  # FIPS code
    cd115fp = db.Column(db.String(2), index=True)  # FIPS code

    # Added manually
    state_name = db.Column(db.String(50))
    state_code = db.Column(db.String(2), index=True)
    district_code = db.Column(db.String(4), index=True)

    geoid = db.Column(db.String(4))
    namelsad = db.Column(db.String(41))
    lsad = db.Column(db.String(2))
    cdsessn = db.Column(db.String(3))
    mtfcc = db.Column(db.String(5))
    funcstat = db.Column(db.String(1))
    aland = db.Column(postgresql.DOUBLE_PRECISION)
    awater = db.Column(postgresql.DOUBLE_PRECISION)
    intptlat = db.Column(db.String(11))
    intptlon =  db.Column(db.String(12))
    geog = db.Column(Geography('MultiPolygon', srid=SRID))

class Rep(db.Model):
    class Chamber(object):
        HOUSE = 'h'
        SENATE = 's'
    class Status(object):
        ACTIVE = 'a'
        LEFT_CONGRESS = 'l'
        DEFEATED_IN_GENERAL = 'd'
        DEFEATED_IN_PRIMARY = 'e'
        RETIRING = 'r'
        SEEKING_OTHER_OFFICE = 'o'
        PENDING_RESULT = 'p'

    rep_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100))
    last_name = db.Column(db.String(100))
    state_code = db.Column(db.String(2), index=True)
    district_number = db.Column(db.Integer, index=True)
    district_code = db.Column(db.String(4), index=True)
    party_code = db.Column(db.String(1), index=True)
    chamber = db.Column(db.String(1), index=True)
    email_link = db.Column(db.String(100))
    email = db.Column(db.String(100))
    website = db.Column(db.String(255))
    address_dc = db.Column(db.String(255))
    phone_dc = db.Column(db.String(20))
    bioguide_id = db.Column(db.String(10))
    status = db.Column(db.String(1), index=True)
    status_note = db.Column(db.String(100))

    def state_name(self):
        return fips.get_state_name_for_code(self.state_code)

    def district_ordinal(self):
        if self.chamber == self.Chamber.HOUSE:
            return text.ordinal(self.district_number) if self.district_number > 0 else 'At-Large'
        return None

class Reminder(db.Model):
    class Frequency(object):
        WEEKLY = 'w'
        MONTHLY = 'm'
    class Status(object):
        ACTIVE = 'a'
        UNSUBSCRIBED = 'u'

    reminder_id = db.Column(db.BigInteger, primary_key=True)
    email = db.Column(db.String(100), index=True)
    frequency = db.Column(db.String(1), index=True)
    status = db.Column(db.String(1), index=True)
    last_contacted = db.Column(db.DateTime(timezone=True), index=True)
    time_created = db.Column(db.DateTime(timezone=True))
    time_updated = db.Column(db.DateTime(timezone=True))
