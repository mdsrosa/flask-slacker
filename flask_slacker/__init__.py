"""
    flask_slacker
    ~~~~~~~~~~~~~

    A Flask extension for using Slacker.

    :copyright: (c) 2017 Matheus Rosa
    :license: MIT, see LICENSE for more details.
"""
from slacker import Slacker as BaseSlacker


__version__ = '0.0.1'


class Slacker(object):
    def __init__(self, app=None, **kwargs):
        """Initialize the Slacker interface.

        :param app: Flask application
        """
        if app is not None:
            self.init_app(app)

    def init_app(self, app, config=None):
        """
        Initialize the app in Flask.
        """
        if not (config is None or isinstance(config, dict)):
            raise ValueError("`config` must be an instance of dict or None")

        # register application within app
        app.extensions = getattr(app, 'extensions', {})
        app.extensions['slack'] = BaseSlacker(**config)
