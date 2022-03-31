from flask import Flask
def create_app(test_config=None):
    app = Flask(__name__, static_url_path="/")
#The app should serve any static resources from the root directory and not from the default /static directory.
    app.url_map.strict_slashes = False
#trailing slashes are optional
    app.config.from_mapping(
        SECRET_KEY='super_secret_key'
#app should use the key when creating server-side sessions
    )

    return app 

#We use a from...import statement to import the Flask() function and then use the def keyword to define a create_app() function.