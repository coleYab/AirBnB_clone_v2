#!/usr/bin/python3
"""
0-hello route: module to do the text.
runs: hbnb
"""
from flask import Flask
from markupsafe import escape
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """
    hello_hbnb: runs hbnb at the root
    args: none
    """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    hello_hbnb: runs hbnb at the root
    args: none
    """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_is(text: str):
    """
    hello_hbnb: runs hbnb at the root
    args: none
    """
    return f"C {escape(text.replace('_', ' '))}"


if __name__ == '__main__':
    """
    runs the applications
    """
    app.run(host='0.0.0.0', port=5000)
