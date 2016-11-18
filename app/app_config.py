import logging

from config import constants
from database import db
from util import sendgrid_

class AppConfig(object):
    SECRET_KEY = constants.FLASK_SECRET_KEY
    CSRF_ENABLED = True

    SQLALCHEMY_DATABASE_URI = constants.SQLALCHEMY_DATABASE_URI
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = False

def init_app(app):
    db.init_app(app)

def init_prod_app(app):
    app.config.from_object(__name__ + '.AppConfig')
    init_app(app)

    if not constants.DEBUG:
        setup_log_handlers(app)
    return app

def setup_log_handlers(app):
    log_level = logging.WARNING
    log_formatter = logging.Formatter(
        '%(asctime)s %(levelname)s [in %(pathname)s:%(lineno)d]: %(message)s')
    log_handlers = [
        logging.FileHandler(constants.APP_LOG_FILENAME),
        new_smtp_log_handler(),
        ]
    app.logger.setLevel(log_level)
    for log_handler in log_handlers:
        log_handler.setLevel(log_level)
        log_handler.setFormatter(log_formatter)
        app.logger.addHandler(log_handler)
    return app

def new_smtp_log_handler():
    return sendgrid_.SendgridEmailLogHandler(
        None,  # No server needed, we're using sendgrid instead of STMP
        None,
        constants.MONITORING_NOTIFICATION_EMAILS,
        'WriteToGov Error')
