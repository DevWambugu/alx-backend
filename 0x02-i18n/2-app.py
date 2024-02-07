#!/usr/bin/env python3
'''2-app'''


from flask import Flask, render_template, request
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)

SUPPORTED_LANGUAGES = ['en', 'fr']

@babel.localeselector
def get_locale():
    '''This function uses request.accept_languages
    to determine the best match with our supported languages.
    '''
    return request.accept_languages.best_match(SUPPORTED_LANGUAGES)

@app.route('/', strict_slashes=False)
def index():
    '''This function returns the home page'''
    return render_template('2-index.html')

if __name__ == "__main__":
    app.run(debug=True)
