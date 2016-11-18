import os

DEBUG = False

HOST = None
HTTPS = True

PROJECTPATH = os.environ.get('PROJECTPATH')

FLASK_SECRET_KEY = None

APP_LOG_FILENAME = os.path.join(PROJECTPATH, 'app.log')

SQLALCHEMY_DATABASE_URI = 'postgresql://localhost/<my-project>'

TEMPLATE_ROOT = os.path.join(PROJECTPATH, 'templates')
STATIC_ROOT = os.path.join(PROJECTPATH, 'static')

PDF_FONT_FILE = os.path.join(PROJECTPATH, 'data/fonts/cmunrm.ttf')
REP_AUTOCOMPLETE_DATA_FNAME = os.path.join(PROJECTPATH, 'data/rep_autocomplete.20161115.json')
PROPUBLICA_API_KEY = None

INTERNAL_IPS = ()

try:
    from constants_override import *
except ImportError:
    pass
