import flask_testing

from app import MyFlask
from app import app
from app import app_config
from database import db
from util import patches
assert patches  # Silence pyflakes

_real_db_app_configured = False

class RealDatabaseTest(flask_testing.TestCase):
    def create_app(self):
        global _real_db_app_configured
        if not _real_db_app_configured:
            app_config.init_prod_app(app)
            _real_db_app_configured = True
        return app

# To use this, you must first create a Postgres DB called 'unittest',
# then connect to it using psql and run 'CREATE EXTENSION postgis;'
#
# Note this uses a completely artifical app merely to set up an
# environment, and no view routes are registered on the dummy app
# used in this case.
class FakeDatabaseTest(flask_testing.TestCase):
    SQLALCHEMY_DATABASE_URI = 'postgres://localhost/unittest'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    TESTING = True
    SECRET_KEY = 'secret_key'
    WTF_CSRF_ENABLED = False

    RERAISE_API_EXCEPTIONS = True
    CREATE_DEFAULT_APP_CONTEXT = True

    def create_app(self):
        fake_db_app = self.fake_db_app = MyFlask('fake_db_test')
        fake_db_app.config.from_object(self)
        app_config.init_app(fake_db_app)
        return fake_db_app

    def setUp(self):
        def cleanup_db():
            db.session.remove()
            db.drop_all()
            db.engine.dispose()
            if self.app_context:
                self.app_context.pop()
        self.addCleanup(cleanup_db)

        db.create_all()
        if self.CREATE_DEFAULT_APP_CONTEXT:
            self.app_context = self.fake_db_app.test_request_context('/testing')
            self.app_context.push()
            app.preprocess_request()
        else:
            self.app_context = None
