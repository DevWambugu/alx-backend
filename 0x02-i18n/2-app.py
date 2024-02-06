#!/usr/bin/env python3
'''2-app'''


from flask import Flask, render_template, request
from flask_babel import Babel, _

app = Flask(__name__)
babel = Babel(app)

