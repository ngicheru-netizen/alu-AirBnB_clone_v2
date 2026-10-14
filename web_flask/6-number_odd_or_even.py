#!/usr/bin/python3
"""Flask application rendering number parity with a template."""

from flask import Flask, render_template


app = Flask(__name__)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def number_odd_or_even(n):
    """Render whether a number is even or odd."""
    return render_template("6-number_odd_or_even.html", number=n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
