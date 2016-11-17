from flask import Flask

from config import constants

class MyFlask(Flask):
    def get_send_file_max_age(self, name):
        if name.startswith('js/') or name.startswith('css/'):
            return 0
        return super(MyFlask, self).get_send_file_max_age(name)

    # Temporary workaround for https://github.com/pallets/flask/pull/1910
    # If you access the jinja_env during startup, then template reloading
    # doesn't necessarily get enabled. We don't actually explictly
    # reference jinja_env during startup, we simply register a custom filter,
    # so unclear why this triggers the bug, but I guess filter registration
    # requires the jinja_env.
    def create_jinja_environment(self):
        self.config['TEMPLATES_AUTO_RELOAD'] = constants.DEBUG
        return super(MyFlask, self).create_jinja_environment()

app = MyFlask(__name__,
    template_folder=constants.TEMPLATE_ROOT,
    static_folder=constants.STATIC_ROOT)
