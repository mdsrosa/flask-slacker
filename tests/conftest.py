from flask import Flask

import pytest


class Config(object):
    SLACKER_TOKEN = 'my-token'
    SLACKER_TIMEOUT = 10


def create_app(config=None):
    app = Flask('testapp')
    app.config.from_object(config)
    return app


@pytest.fixture
def config():
    return Config()


@pytest.fixture
def app(request, config):
    app = create_app(config)
    ctx = app.app_context()
    ctx.push()

    def teardown():
        ctx.pop()

    request.addfinalizer(teardown)
    return app


@pytest.fixture
def app_missing_config(request):
    app = create_app()
    ctx = app.app_context()
    ctx.push()

    def teardown():
        ctx.pop()

    request.addfinalizer(teardown)
    return app
