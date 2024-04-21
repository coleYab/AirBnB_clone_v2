#!/usr/bin/python3
"""
0-hello route: module to do the text.
runs: hbnb
"""
from flask import Flask, render_template
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


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_is(text="is_cool"):
    """
    hello_hbnb: runs hbnb at the root
    args: none
    """
    return f"Python {escape(text.replace('_', ' '))}"


@app.route('/number/<int:number>', strict_slashes=False)
def display_number(number):
    """
    hello_hbnb: runs hbnb at the root
    args: none
    """
    return f"{number} is a number"


@app.route('/number_template/<int:number>', strict_slashes=False)
def display_number_(number):
    """
    hello_hbnb: runs hbnb at the root
    args: none
    """
    return render_template('5-number.html', no=number)


if __name__ == '__main__':
    """
    runs the applications
    """
    app.run(host='0.0.0.0', port=5000)
