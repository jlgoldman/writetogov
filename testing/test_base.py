import flask_testing

from app import app
from app import app_config
from util import patches
assert patches  # Silence pyflakes

_app_configured = False

class RealDatabaseTest(flask_testing.TestCase):
    def create_app(self):
        global _app_configured
        if not _app_configured:
            app_config.init_prod_app(app)
            _app_configured = True
        return app
