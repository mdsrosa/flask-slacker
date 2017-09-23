"""
    flask_slacker
    ~~~~~~~~~~~~~

    A Flask extension for using Slacker.

    :copyright: (c) 2017 Matheus Rosa
    :license: MIT, see LICENSE for more details.
"""
from slacker import Slacker as BaseSlacker, DEFAULT_TIMEOUT


__version__ = '0.0.1'


class Slacker(object):
    def __init__(self, app=None):
        """Initialize the Slacker interface.

        :param app: Flask application
        """
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        """
        Initialize the app in Flask.
        """
        app.config.setdefault('SLACKER_TIMEOUT', DEFAULT_TIMEOUT)

        if 'SLACKER_TOKEN' not in app.config:
            raise Exception('Missing SLACKER_TOKEN in your config.')

        token = app.config['SLACKER_TOKEN']
        timeout = app.config['SLACKER_TIMEOUT']

        # register application within app
        app.extensions = getattr(app, 'extensions', {})
        app.extensions['slack'] = BaseSlacker(token, timeout=timeout)
