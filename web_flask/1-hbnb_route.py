#!/usr/bin/python3
"""
A script that starts a Flask web application
Web application must be listening on 0.0.0.0, port 5000
Display “Hello HBNB!”
Display “HBNB”
"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """
    Returns 'Hello HBNB!'
    """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    Returns HBNB
    """
    return 'HBNB'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
