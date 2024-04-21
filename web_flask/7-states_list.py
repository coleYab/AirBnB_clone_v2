#!/usr/bin/python3
"""
0-hello route: module to do the text.
runs: hbnb
"""
from flask import Flask, render_template
from markupsafe import escape
from models import storage
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


@app.route('/number_odd_or_even/<int:number>', strict_slashes=False)
def number_odd_or_even(number):
    """
    hello_hbnb: runs hbnb at the root
    args: none
    """
    text_ = ''
    if number % 2 == 1:
        text_ = f"{number} is odd"
    else:
        text_ = f"{number} is even"
    return render_template('6-number_odd_or_even.html', text=text_)


@app.route('/states_list', strict_slashes=False)
def route_states():
    """
    route_states: displays all the available states
    """
    states_list = storage.all('State')
    return render_template('7-states_list.html', states=states_list)


@app.teardown_appcontext
def close_storage(exception=None):
    """
    closes a function for the code.
    """
    storage.close()


if __name__ == '__main__':
    """
    runs the applications
    """
    app.run(host='0.0.0.0', port=5000)
