#!/usr/bin/python3
"""Display states, optionally filtered by ID."""

from flask import Flask, render_template, request

from models import storage
from models.state import State


app = Flask(__name__)


@app.teardown_appcontext
def close_storage(exception):
    """Close the current storage session after each request."""
    storage.close()


@app.route("/states", strict_slashes=False)
def states():
    """Render all states or the state selected by query parameter."""
    state_id = request.args.get("id")
    all_states = storage.all(State).values()
    if state_id:
        all_states = [
            state for state in all_states if state.id == state_id
        ]
    states = sorted(all_states, key=lambda state: state.name)
    return render_template("9-states.html", states=states)


@app.route("/states/<state_id>", strict_slashes=False)
def state_by_id(state_id):
    """Render the state selected by its ID."""
    states = [
        state for state in storage.all(State).values()
        if state.id == state_id
    ]
    return render_template("9-states.html", states=states)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
