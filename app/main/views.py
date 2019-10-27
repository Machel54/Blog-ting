from flask import render_template,redirect,url_for
from . import main
from flask_bootstrap import Bootstrap
# from ..requests import getQuotes

# Views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    title = 'Home - Blog yeah'

    return render_template('index.html', title = title)


