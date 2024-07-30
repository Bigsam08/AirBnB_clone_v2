#!/usr/bin/python3
""" make flask run listening on 0.0.0.0 @ port 5000
    display a message
"""

from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def airbnb():
    return 'Hello HBNB!'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
