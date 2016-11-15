import collections

FIPSInfo = collections.namedtuple('FIPSInfo', ['name', 'fips_code', 'state_code'])

def get_by_fips_code(fips_code):
    return INFOS_BY_FIPS_CODE.get(fips_code)

def get_by_state_code(state_code):
    return INFOS_BY_STATE_CODE.get(state_code)

def get_state_name_for_code(state_code):
    fips_info = get_by_state_code(state_code)
    return fips_info.name if fips_info else None

FIPS_INFOS = map(lambda t: FIPSInfo(*t), (
    ('Alabama',                    '01', 'AL'),
    ('Alaska',                     '02', 'AK'),
    ('Arizona',                    '04', 'AZ'),
    ('Arkansas',                   '05', 'AR'),
    ('California',                 '06', 'CA'),
    ('Colorado',                   '08', 'CO'),
    ('Connecticut',                '09', 'CT'),
    ('Delaware',                   '10', 'DE'),
    ('District of Columbia',       '11', 'DC'),
    ('Florida',                    '12', 'FL'),
    ('Georgia',                    '13', 'GA'),
    ('Hawaii',                     '15', 'HI'),
    ('Idaho',                      '16', 'ID'),
    ('Illinois',                   '17', 'IL'),
    ('Indiana',                    '18', 'IN'),
    ('Iowa',                       '19', 'IA'),
    ('Kansas',                     '20', 'KS'),
    ('Kentucky',                   '21', 'KY'),
    ('Louisiana',                  '22', 'LA'),
    ('Maine',                      '23', 'ME'),
    ('Maryland',                   '24', 'MD'),
    ('Massachusetts',              '25', 'MA'),
    ('Michigan',                   '26', 'MI'),
    ('Minnesota',                  '27', 'MN'),
    ('Mississippi',                '28', 'MS'),
    ('Missouri',                   '29', 'MO'),
    ('Montana',                    '30', 'MT'),
    ('Nebraska',                   '31', 'NE'),
    ('Nevada',                     '32', 'NV'),
    ('New Hampshire',              '33', 'NH'),
    ('New Jersey',                 '34', 'NJ'),
    ('New Mexico',                 '35', 'NM'),
    ('New York',                   '36', 'NY'),
    ('North Carolina',             '37', 'NC'),
    ('North Dakota',               '38', 'ND'),
    ('Ohio',                       '39', 'OH'),
    ('Oklahoma',                   '40', 'OK'),
    ('Oregon',                     '41', 'OR'),
    ('Pennsylvania',               '42', 'PA'),
    ('Rhode Island',               '44', 'RI'),
    ('South Carolina',             '45', 'SC'),
    ('South Dakota',               '46', 'SD'),
    ('Tennessee',                  '47', 'TN'),
    ('Texas',                      '48', 'TX'),
    ('Utah',                       '49', 'UT'),
    ('Vermont',                    '50', 'VT'),
    ('Virginia',                   '51', 'VA'),
    ('Washington',                 '53', 'WA'),
    ('West Virginia',              '54', 'WV'),
    ('Wisconsin',                  '55', 'WI'),
    ('Wyoming',                    '56', 'WY'),

    ('American Samoa',             '60', 'AS'),
    ('Guam',                       '66', 'GU'),
    ('Northern Mariana Islands',   '69', 'MP'),
    ('Puerto Rico',                '72', 'PR'),
    ('Virgin Islands of the U.S.', '78', 'VI'),
))

INFOS_BY_FIPS_CODE = {t[1]: t for t in FIPS_INFOS}
INFOS_BY_STATE_CODE = {t[2]: t for t in FIPS_INFOS}
