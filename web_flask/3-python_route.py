#!/usr/bin/python3
"""
A script that starts a Flask web application
Web application must be listening on 0.0.0.0, port 5000
Display “Hello HBNB!”
Display “HBNB”
Display “Python ”, followed by the value of the text variable
Default value of text is “is cool
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


@app.route('/c/<text>', strict_slashes=False)
def c_route(text):
    """
    Display "C" followed by the value of the text variable
    """
    return "C %s" % text.replace('_', ' ')


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_route(text):
    """
    Called through /python/<text> route.
    """
    return 'Python {}'.format(text.replace('_', ' '))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
