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

    def init_app(self, app, config=None, session=None):
        """
        Initialize the app in Flask.
        """
        app.config.setdefault('SLACKER_TIMEOUT', DEFAULT_TIMEOUT)
        app.config.setdefault('SLACKER_HTTP_PROXY', None)
        app.config.setdefault('SLACKER_HTTPS_PROXY', None)

        if config is None:
            config = app.config

        if 'SLACKER_TOKEN' not in config:
            raise Exception('Missing SLACKER_TOKEN in your config.')

        token = config['SLACKER_TOKEN']
        timeout = config['SLACKER_TIMEOUT']
        http_proxy = config['SLACKER_HTTP_PROXY']
        https_proxy = config['SLACKER_HTTPS_PROXY']

        self._slacker = BaseSlacker(token, timeout=timeout, http_proxy=http_proxy,
                                    https_proxy=https_proxy, session=session)

        # set Slacker attributes
        attrs = filter(lambda a: '_' not in a, dir(self._slacker))
        for attr in attrs:
            setattr(self, attr, getattr(self._slacker, attr))

        # register application within app
        app.extensions = getattr(app, 'extensions', {})
        app.extensions['slacker'] = self
