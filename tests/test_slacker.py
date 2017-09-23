import pytest
from flask_slacker import Slacker


def test_init_app(app, config):
    slacker = Slacker()

    assert 'slacker' not in app.extensions

    slacker.init_app(app)

    assert 'slacker' in app.extensions


def test_init_app_missing_config(app_missing_config):
    slacker = Slacker()

    with pytest.raises(Exception) as e:
        slacker.init_app(app_missing_config)
        assert 'SLACKER_TOKEN' in e


def test_slacker_attributes(app, config):
    slacker = Slacker()
    slacker.init_app(app)

    assert 'slacker' in app.extensions
    assert app.extensions['slacker'] is not None
    assert slacker.chat is not None
    assert slacker.users is not None
