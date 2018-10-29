Flask-Slacker
=============
.. image:: https://travis-ci.org/mdsrosa/flask-slacker.svg?branch=master
    :target: https://travis-ci.org/mdsrosa/flask-slacker
    :alt: Test Status

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
    from flask_slacker import Slacker

    def create_app():
        app = Flask(__name__)

        slacker = Slacker(token='my-super-secret-token')
        slacker.init_app(app)

        # more here..
        return app

.. _`application factory`: http://flask.pocoo.org/docs/0.10/patterns/appfactories/

You can also set ``SLACKER_TOKEN`` as an environment variable so you don't have to pass the ``token`` argument to the ``Slacker`` class:

.. code-block:: python

    from flask import Flask
    from flask_slacker import Slacker

    def create_app():
        app = Flask(__name__)

        slacker = Slacker()
        slacker.init_app(app)

        return app


Examples
--------

.. code-block:: python

    from http import HTTPStatus
    from flask import Flask, request, jsonify
    from flask_slacker import Slacker

    app = Flask(__name__)
    slacker = Slacker(app, token="my-super-secret-token")
    # slacker = Slacker()  # reading from environment

    @app.route("/send_notification", methods=["POST"])
    def send_notification():
        data = request.get_json()
        channel = data.get("channel", "#random")
        username = data.get("username")
        message = data.get("message")

        slacker.chat.post_message(
            channel, message,
            username=username
        )
        response = {"message": f"Slack message sent to #{channel}!"}
        return jsonify(response), HTTPStatus.CREATED


    if __name__ == "__main__":
        app.run(host="0.0.0.0", port=5000)


And here is the response using `httpie`_:

.. code-block:: console

    $ http POST http://localhost:5000/send_notification message=testing username=matheus channel=random
    HTTP/1.0 201 CREATED
    Content-Length: 28
    Content-Type: application/json
    Date: Mon, 29 Oct 2018 17:05:38 GMT
    Server: Werkzeug/0.14.1 Python/3.7.0

    {
        "message": "Slack message sent to #random"
    }

.. _`httpie`: https://httpie.org/