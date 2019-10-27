from flask import render_template
from . import main
from flask_bootstrap import Bootstrap

# Views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    title = 'Home - Blog yeah'

    return render_template('index.html', title = title)


