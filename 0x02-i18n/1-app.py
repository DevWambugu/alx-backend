#!/usr/bin/env python3
'''1-app'''


from flask import Flask
from flask_babel import Babel

app = Flask(__name__)


class Config:
    '''This class LANGUAGES class
    attribute equal to ["en", "fr"]'''
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)

babel = Babel(app)
