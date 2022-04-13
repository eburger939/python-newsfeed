from app.routes import home, dashboard
#importing bp that was renamed as home within the routes init.py file 
#other way of writing if it wasn't already imported/renamed:
#from app.routes.home import bp as home 
from flask import Flask
from app.db import init_db
from app.utils import filters


def create_app(test_config=None):
    app = Flask(__name__, static_url_path="/")
#The app should serve any static resources from the root directory and not from the default /static directory.
    app.url_map.strict_slashes = False
#trailing slashes are optional
    app.config.from_mapping(
        SECRET_KEY='super_secret_key'
#app should use the key when creating server-side sessions
    )
    app.jinja_env.filters['format_url'] = filters.format_url
    app.jinja_env.filters['format_date'] = filters.format_date
    app.jinja_env.filters['format_plural'] = filters.format_plural


#We use a from...import statement to import the Flask() function and then use the def keyword to define a create_app() function.


    @app.route('/hello')
    def hello():
        return 'hello world'
    app.register_blueprint(home)
    app.register_blueprint(dashboard)
    init_db(app)
    return app  
#when visiting 127.0.0.1:5000/hello the page will return hello world 