from fixture import DataSet
from fixture import SQLAlchemyFixture

from database import db
from database import db_models

class RepData(DataSet):
    class nancy_pelosi(object):
        rep_id          = 134
        first_name      = 'Nancy'
        last_name       = 'Pelosi'
        state_code      = 'CA'
        district_number = 12
        district_code   = 'CA12'
        party_code      = 'D'
        chamber         = db_models.Rep.Chamber.HOUSE
        email_link      = None
        email           = None
        website         = None
        address_dc      = '233 Longworth House Office Building Washington DC, 20515'
        phone_dc        = '(202) 225-4965'
        bioguide_id     = 'P000197'
        status          = db_models.Rep.Status.ACTIVE
        status_note     = None
    class dianne_feinstein(object):
        rep_id          = 33
        first_name      = 'Dianne'
        last_name       = 'Feinstein'
        state_code      = 'CA'
        district_number = None
        district_code   = None
        party_code      = 'D'
        chamber         = db_models.Rep.Chamber.SENATE
        email_link      = 'https://www.feinstein.senate.gov/public/index.cfm/e-mail-me'
        email           = None
        website         = 'http://www.feinstein.senate.gov'
        address_dc      = '331 Hart Senate Office Building Washington DC, 20510'
        phone_dc        = '(202) 224-3841'
        bioguide_id     = 'F000062'
        status          = db_models.Rep.Status.ACTIVE
        status_note     = None
    class barbara_boxer(object):
        rep_id          = 10
        first_name      = 'Barbara'
        last_name       = 'Boxer'
        state_code      = 'CA'
        district_number = None
        district_code   = None
        party_code      = 'D'
        chamber         = db_models.Rep.Chamber.SENATE
        email_link      = 'https://www.boxer.senate.gov/?p=shareyourviews'
        email           = None
        website         = 'http://www.boxer.senate.gov'
        address_dc      = '112 Hart Senate Office Building Washington DC, 20510'
        phone_dc        = '(202) 224-3553'
        bioguide_id     = 'B000711'
        status          = db_models.Rep.Status.RETIRING
        status_note     = 'Announced retirement on Jan. 8, 2015'
    class mitch_mcconnell(object):
        rep_id          = 61
        first_name      = 'Mitch'
        last_name       = 'McConnell'
        state_code      = 'KY'
        district_number = None
        district_code   = None
        party_code      = 'R'
        chamber         = db_models.Rep.Chamber.SENATE
        email_link      = 'http://www.mcconnell.senate.gov/public/index.cfm?p=contact'
        email           = None
        website         = 'http://www.mcconnell.senate.gov/'
        address_dc      = '317 Russell Senate Office Building Washington DC, 20510'
        phone_dc        = '(202) 224-2541'
        bioguide_id     = 'M000355'
        status          = db_models.Rep.Status.ACTIVE
        status_note     = None
    class paul_ryan(object):
        rep_id          = 530
        first_name      = 'Paul'
        last_name       = 'Ryan'
        state_code      = 'WI'
        district_number = 1
        district_code   = 'WI01'
        party_code      = 'R'
        chamber         = db_models.Rep.Chamber.HOUSE
        email_link      = None
        email           = None
        website         = None
        address_dc      = '1233 Cannon House Office Building Washington DC, 20515'
        phone_dc        = '(202) 225-3031'
        bioguide_id     = 'R000570'
        status          = db_models.Rep.Status.ACTIVE
        status_note     = None
    class cynthia_lummis(object):
        rep_id          = 541
        first_name      = 'Cynthia'
        last_name       = 'Lummis'
        state_code      = 'WY'
        district_number = 0
        district_code   = 'WY00'
        party_code      = 'R'
        chamber         = db_models.Rep.Chamber.HOUSE
        email_link      = None
        email           = None
        website         = None
        address_dc      = '2433 Rayburn House Office Building Washington DC, 20515'
        phone_dc        = '(202) 225-2311'
        bioguide_id     = 'L000571'
        status          = db_models.Rep.Status.RETIRING
        status_note     = 'Announced retirement on Nov. 12, 20'
    class john_barrasso(object):
        rep_id          = 4
        first_name      = 'John'
        last_name       = 'Barrasso'
        state_code      = 'WY'
        district_number = None
        district_code   = None
        party_code      = 'R'
        chamber         = db_models.Rep.Chamber.SENATE
        email_link      = 'https://www.barrasso.senate.gov/public/index.cfm/contact-form'
        email           = None
        website         = 'http://www.barrasso.senate.gov'
        address_dc      = '307 Dirksen Senate Office Building Washington DC, 20510'
        phone_dc        = '(202) 224-6441'
        bioguide_id     = 'B001261'
        status          = db_models.Rep.Status.ACTIVE
        status_note     = None
    class michel_enzi(object):
        rep_id          = 31
        first_name      = 'Michael B.'
        last_name       = 'Enzi'
        state_code      = 'WY'
        district_number = None
        district_code   = None
        party_code      = 'R'
        chamber         = db_models.Rep.Chamber.SENATE
        email_link      = 'http://www.enzi.senate.gov/public/index.cfm/contact?p=e-mail-senator-enzi'
        email           = None
        website         = 'http://www.enzi.senate.gov'
        address_dc      = '379A Russell Senate Office Building Washington DC, 20510'
        phone_dc        = '(202) 224-3424'
        bioguide_id     = 'E000285'
        status          = db_models.Rep.Status.ACTIVE
        status_note     = None
    class vacant_ky01(object):
        rep_id          = 271
        first_name      = None
        last_name       = None
        state_code      = 'KY'
        district_number = 1
        district_code   = 'KY01'
        party_code      = None
        chamber         = db_models.Rep.Chamber.HOUSE
        email_link      = None
        email           = None
        website         = None
        address_dc      = '2184 Rayburn House Office Building Washington DC, 20515'
        phone_dc        = '(202) 225-3115'
        bioguide_id     = None
        status          = db_models.Rep.Status.LEFT_CONGRESS
        status_note     = 'Announced resignation effective Sept. 6, 2016.'
    class rand_paul(object):
        rep_id          = 70
        first_name      = 'Rand'
        last_name       = 'Paul'
        state_code      = 'KY'
        district_number = None
        district_code   = None
        party_code      = 'R'
        chamber         = db_models.Rep.Chamber.SENATE
        email_link      = 'https://www.paul.senate.gov/connect/email-rand'
        email           = None
        website         = 'http://www.paul.senate.gov'
        address_dc      = '167 Russell Senate Office Building Washington DC, 20510'
        phone_dc        = '(202) 224-4343'
        bioguide_id     = 'P000603'
        status          = db_models.Rep.Status.ACTIVE
        status_note     = None

class DistrictData(DataSet):
    class wy00(object):
        gid           = 7
        statefp       = '56'
        cd115fp       = '00'
        geoid         = '5600'
        namelsad      = 'Congressional District (at Large)'
        lsad          = 'C1'
        cdsessn       = '115'
        mtfcc         = 'G5200'
        funcstat      = 'N'
        aland         = 251464935120
        awater        = 1861273298
        intptlat      = '+42.9918024'
        intptlon      = '-107.5419255'
        state_name    = 'Wyoming'
        state_code    = 'WY'
        district_code = 'WY00'
        # Simplified polygon for testing
        geog          = 'MULTIPOLYGON(((-111.054556 45.000955,-104.057879 44.997605,-104.053249 41.001406,-111.046815 40.997875,-111.054556 45.000955)))'

def setup_testdata():
    dbfixture = SQLAlchemyFixture(
        engine=db.engine,
        env={
            'RepData': db_models.Rep,
            'DistrictData': db_models.District,
            })
    fixture_datas = [
        dbfixture.data(RepData, DistrictData),
        ]
    return dbfixture, fixture_datas
