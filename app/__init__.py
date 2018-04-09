from flask import Flask
from flask_bootstrap import Bootstrap
from config import config_options


bootstrap = Bootstrap()

def create_app(config_name):
    #Initializing application
    app = Flask(__name__)

    #Creating the app configurations
    app.config.from_object(config_options[config_name])

    #Initializing Flask Extensions
    bootstrap.init_app(app)

    #Will add the views and forms
def create_app(config_name):
    #Registering the blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    #setting config
    from .request import configure_request
    configure_request(app)

    return app

#Setting up configuration
# app.config.from_object(DevConfig)
# app.config.from_pyfile('config.py')
#


# from app import views
