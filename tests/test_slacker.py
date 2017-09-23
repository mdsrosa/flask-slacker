import pytest
from flask_slacker import Slacker


def test_init_app(app, config):
    slack = Slacker()

    assert 'slack' not in app.extensions

    slack.init_app(app)

    assert 'slack' in app.extensions
    assert app.extensions.get('slack') is not None


def test_init_app_missing_config(app_missing_config):
    slack = Slacker()

    assert 'slack' not in app_missing_config.extensions

    with pytest.raises(Exception) as e:
        slack.init_app(app_missing_config)

        assert 'SLACKER_TOKEN' in e
