#!/usr/bin/python3
"""
script that start a Flask web application:
- web application must be listening on 0.0.0.0, port 5000
- Hello 
"""

from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_HBNB():
    """Flask web application that displays 'Hello HBNB'"""
    return "Hello HBNB!"


if __name__ == "__main__":
    app.run()HBNB!display 
