import pytest

from flask_slacker import Slacker


def test_init_app(app, config, app_missing_config):
    slacker = Slacker()

    assert "slacker" not in app.extensions

    slacker.init_app(app)

    assert "slacker" in app.extensions

    # test app without config but specifies token
    slacker = Slacker(app_missing_config, token="my-token")

    assert "slacker" in app.extensions


def test_init_app_missing_config(app_missing_config):
    slacker = Slacker()

    with pytest.raises(LookupError) as e:
        slacker.init_app(app_missing_config)
        assert "SLACKER_TOKEN" in e


def test_slacker_attributes(app, config):
    slacker = Slacker()
    slacker.init_app(app)

    assert "slacker" in app.extensions
    assert app.extensions["slacker"] is not None
    assert slacker.chat
    assert slacker.users
