#!/usr/bin/python3
"""Flask application rendering number parity."""

from flask import Flask, render_template


app = Flask(__name__)


@app.route("/number/<int:n>", strict_slashes=False)
def number_template(n):
    """Render whether a number is even or odd."""
    return render_template("5-number.html", number=n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
