Flask-Slacker
=============
.. image:: https://travis-ci.org/mdsrosa/flask-slacker.svg?branch=master
   :target: https://travis-ci.org/mdsrosa/flask-slacker
   :alt: Tests Status

.. image:: https://coveralls.io/repos/github/mdsrosa/flask-slacker/badge.svg?branch=master
   :target: https://coveralls.io/github/mdsrosa/flask-slacker?branch=master
   :alt: Test Coverage Status

.. snip

A Flask extension for Slacker_.

.. _`Slacker`: https://github.com/os/slacker

Installation
------------

.. code-block:: console

    pip install Flask-Slacker

Getting started
---------------

To quickly start using Flask-Slacker, simply create a ``Slacker`` instance:


.. code-block:: python

    from flask import Flask
    from flask_slacker import Slacker

    app = Flask(__name__)
    slacker = Slacker(app, token='my-token')

Alternatively, if you're using the `application factory`_ pattern:

.. code-block:: python

    from flask_slacker import Slacker
    slacker = Slacker(token='my-token')

and then later call ``init_app`` where you create your application object:

.. code-block:: python

    from flask import Flask

    def create_app():
        app = Flask(__name__)

        slacker.init_app(app)

        # more here..
        return app

.. _`application factory`: http://flask.pocoo.org/docs/0.10/patterns/appfactories/
