import flask_sqlalchemy
import flask_testing
from sqlalchemy import orm

from app import app
from app import app_config
from database import db
from testing import test_data
from util import patches
assert patches  # Silence pyflakes

# To use this, you must first create a Postgres DB called 'unittest',
# then connect to it using psql and run 'CREATE EXTENSION postgis;'
class DatabaseWithTestdataTest(flask_testing.TestCase):
    SQLALCHEMY_DATABASE_URI = "postgres://localhost/unittest"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    TESTING = True
    SECRET_KEY = 'secret_key'
    WTF_CSRF_ENABLED = False

    RERAISE_API_EXCEPTIONS = True
    CREATE_DEFAULT_APP_CONTEXT = True

    def create_app(self):
        return self._app

    @classmethod
    def _create_app(cls):
        app.config.from_object(cls)
        app_config.init_app(app)
        return app

    @classmethod
    def setUpClass(cls):
        cls._app = cls._create_app()
        cls._app.app_context().push()
        cls.connection = db.engine.connect()
        cls.transaction = cls.connection.begin()
        db.Model.metadata.create_all(bind=cls.connection)
        dbfixture, testdatas = test_data.setup_testdata(cls.connection)
        for data in testdatas:
            data.setup()

    @classmethod
    def tearDownClass(cls):
        cls.transaction.rollback()
        cls.connection.close()
        db.engine.dispose()

    def setUp(self):
        def cleanup_db():
            self.current_transaction.rollback()
            if self.app_context:
                self.app_context.pop()
        self.addCleanup(cleanup_db)

        self.current_transaction = self.connection.begin_nested()
        db.session = orm.scoped_session(
            orm.sessionmaker(bind=self.connection))

        if self.CREATE_DEFAULT_APP_CONTEXT:
            self.app_context = app.test_request_context('/testing')
            self.app_context.push()
            app.preprocess_request()
        else:
            self.app_context = None
