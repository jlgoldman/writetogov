# Create a file called config/constants_override.py to override
# any of these values with ones specific to your environment.
# constants_override.py is kept out of git so it can contain
# secret keys and local settings that aren't appropriate for the repo.
#
# Suggested default values for constants_override.py:
#
# DEBUG = True
# HOST = 'localhost:5000'
# HTTPS = False
# FLASK_SECRET_KEY = <generate once with os.urandom(24)>
# PUBLIC_ID_ENCRYPTION_KEY = <generate once with os.urandom(24)>
# GOOGLE_MAPS_API_KEY = <generate using steps below>

import os

DEBUG = False  # Set to True for development

HOST = None  # Set to e.g. localhost:5000 or a local proxy like ngrok
HTTPS = True  # Set to False if using localhost in development

PROJECTPATH = os.environ.get('PROJECTPATH')

FLASK_SECRET_KEY = None  # Generate a local secret with import os; os.urandom(24)
PUBLIC_ID_ENCRYPTION_KEY = None  # Generate a local secret with import os; os.urandom(24)

APP_LOG_FILENAME = os.path.join(PROJECTPATH, 'app.log')

SQLALCHEMY_DATABASE_URI = 'postgresql://localhost/writetogov'

TEMPLATE_ROOT = os.path.join(PROJECTPATH, 'templates')
STATIC_ROOT = os.path.join(PROJECTPATH, 'static')

PDF_FONT_FILE = os.path.join(PROJECTPATH, 'data/fonts/cmunrm.ttf')
REP_AUTOCOMPLETE_DATA_FNAME = os.path.join(PROJECTPATH, 'data/rep_autocomplete.20161115.json')

# Register for a Google Cloud Console project, go to the Credentials section,
# generate an API key, and enable Google Maps JavaScript API and
# Google Places API Web Service
GOOGLE_MAPS_API_KEY = None

PROPUBLICA_API_KEY = None  # Only needed for one-time imports of data, not needed for running the server.
SENGRID_API_KEY = None  # Only needed if testing email sending for reminders and subscriptions
STRIPE_SECRET_KEY = None  # Only needed if testing billing for mailing letters using Lob
STRIPE_PUBLISHABLE_KEY = None  # Only needed if testing billing for mailing letters using Lob
LOB_API_KEY = None  # Only needed if testing Lob API calls for mailing letters.

INTERNAL_IPS = ()
MONITORING_NOTIFICATION_EMAILS = ()

def abspath(*path_elements):
    return os.path.join(PROJECTPATH, *path_elements)

try:
    from constants_override import *
except ImportError:
    pass
