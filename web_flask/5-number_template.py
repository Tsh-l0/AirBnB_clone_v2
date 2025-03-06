#!/usr/bin/python3
"""
A script that starts a Flask web application

Web application must be listening on 0.0.0.0, port 5000

Display “Hello HBNB!”

Display “HBNB”

Display “Python ”, followed by the value of the text variable

Default value of text is “is cool

/number/<n>: display “n is a number” only if n is an integer

Display a HTML page only if n is an integer when
/number_template/<n> is called. H1 tag: “Number: n” inside the tag BODY
"""
from flask import Flask
from flask import render_template

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


@app.route('/number/<int:n>', strict_slashes=False)
def number_route(n):
    """
    Displays “n is a number” when /number/<n> is called
    """
    return '{:d} is a number'.format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """
    Displays a HTML page if n is an integer
    """
    return render_template('5-number.html', n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
