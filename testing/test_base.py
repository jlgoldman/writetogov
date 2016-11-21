import flask_testing

from app import MyFlask
from app import app
from app import app_config
from database import db
from testing import test_data
from util import patches
assert patches  # Silence pyflakes

_app_configured = False

# To use this, you must first create a Postgres DB called 'unittest',
# then connect to it using psql and run 'CREATE EXTENSION postgis;'
class DatabaseTest(flask_testing.TestCase):
    SQLALCHEMY_DATABASE_URI = "postgres://localhost/unittest"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    TESTING = True
    SECRET_KEY = 'secret_key'
    WTF_CSRF_ENABLED = False

    RERAISE_API_EXCEPTIONS = True
    CREATE_DEFAULT_APP_CONTEXT = True

    def create_app(self):
        global _app_configured
        if not _app_configured:
            app.config.from_object(self)
            app_config.init_app(app)
            _app_configured = True
        return app

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
            self.app_context = app.test_request_context('/testing')
            self.app_context.push()
            app.preprocess_request()
        else:
            self.app_context = None

class DatabaseWithTestdataTest(DatabaseTest):
    def setUp(self):
        super(DatabaseWithTestdataTest, self).setUp()
        self.dbfixture, self.testdatas = test_data.setup_testdata()
        for data in self.testdatas:
            data.setup()
        def cleanup_testdata():
            # TODO: Figure out why this causes hanging sometimes
            # or if we need this at all.
            # for data in self.testdatas[::-1]:
            #     data.teardown()
            self.dbfixture.dispose()
        self.addCleanup(cleanup_testdata)
