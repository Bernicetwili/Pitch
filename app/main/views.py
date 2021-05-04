from flask import render_template
from . import main
from flask import render_template,request,redirect,url_for



@main.route('/')
def index():
    '''
    my index page
    return
    '''
    message= "Hello"
    return render_template('index.html', message=message)