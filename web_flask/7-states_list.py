#!/usr/bin/env/python3
"""
Starts a Flask web application

Web application must be listening on 0.0.0.0, port 5000

Use storage for fetching data from the storage engine

After each request you must remove the current SQLAlchemy Session
"""
from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)

@app.route("/states_list", strict_slashes=False)
def display_states():
    """
    Return state_list to display States created
    """
    states = storage.all()
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def teardown(self):
    """
    Remove SQLAlchemy session
    """
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
