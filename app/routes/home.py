from flask import Blueprint, render_template
#blueprint allows you to consolidate routes into a single object (bp) that the parent app can register later
#similar to using router middelware when using express.js

bp = Blueprint('home', __name__, url_prefix='/')

@bp.route('/')
#@bp.route before the function turns it into a route 
#adding the decoratory (@bp.route) also allows you to import the function too
def index():
    return render_template('homepage.html')
    #return is the response, using render_template allows to return a template instead of a string
@bp.route('/login')
def login():
    return render_template('login.html')

@bp.route('/post/<id>')
#<id> is basically the same as a parameter in the url route 
def single(id):
    return render_template('single-post.html')