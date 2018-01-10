# Create a .env file with secret keys and such.
#
# Suggested default values for .env:
#
# DEBUG = True
# HOST = 'localhost:5000'
# HTTPS = False
# FLASK_SECRET_KEY = <generate once with os.urandom(24)>
# PUBLIC_ID_ENCRYPTION_KEY = <generate once with os.urandom(24)>
# GOOGLE_MAPS_API_KEY = <generate using steps below>

import os

import dotenv

dotenv_filename = dotenv.find_dotenv()
if dotenv_filename:
    dotenv.load_dotenv(dotenv_filename)

def parse_bool(env_value):
    return env_value is not None and env_value.lower() not in ('0', 'false')

DEBUG = parse_bool(os.environ.get('DEBUG'))  # Set to True for development

HOST = os.environ.get('HOST')  # Set to e.g. localhost:5000 or a local proxy like ngrok
HTTPS = True  # Set to False if using localhost in development

PROJECTPATH = os.environ.get('PROJECTPATH')

FLASK_SECRET_KEY = os.environ.get('FLASK_SECRET_KEY')  # Generate a local secret with import os; os.urandom(24)
PUBLIC_ID_ENCRYPTION_KEY = os.environ.get('PUBLIC_ID_ENCRYPTION_KEY')  # Generate a local secret with import os; os.urandom(24)

APP_LOG_FILENAME = os.path.join(PROJECTPATH, 'app.log')

SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')

TEMPLATE_ROOT = os.path.join(PROJECTPATH, 'templates')
STATIC_ROOT = os.path.join(PROJECTPATH, 'static')

PDF_FONT_FILE = os.path.join(PROJECTPATH, 'data/fonts/cmunrm.ttf')
REP_AUTOCOMPLETE_DATA_FNAME = os.path.join(PROJECTPATH, 'data/rep_autocomplete.20170210.json')

# Register for a Google Cloud Console project, go to the Credentials section,
# generate an API key, and enable Google Maps JavaScript API and
# Google Places API Web Service
GOOGLE_MAPS_API_KEY = None

PROPUBLICA_API_KEY = os.environ.get('PROPUBLICA_API_KEY')  # Only needed for one-time imports of data, not needed for running the server.
SENGRID_API_KEY = os.environ.get('SENGRID_API_KEY')  # Only needed if testing email sending for reminders and subscriptions
STRIPE_SECRET_KEY = os.environ.get('STRIPE_SECRET_KEY')  # Only needed if testing billing for mailing letters using Lob
STRIPE_PUBLISHABLE_KEY = os.environ.get('STRIPE_PUBLISHABLE_KEY')  # Only needed if testing billing for mailing letters using Lob
LOB_API_KEY = os.environ.get('LOB_API_KEY') # Only needed if testing Lob API calls for mailing letters.

INTERNAL_IPS = os.environ.get('INTERNAL_IPS', '').split(',')
MONITORING_NOTIFICATION_EMAILS = os.environ.get('MONITORING_NOTIFICATION_EMAILS', '').split(',')

def abspath(*path_elements):
    return os.path.join(PROJECTPATH, *path_elements)
