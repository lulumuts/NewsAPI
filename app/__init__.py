from flask import Flask
from .config import DevConfig

#Initializing application
app = Flask(__name__,instsance_relative_config = True)

#Setting up configuration
app.config.from_object(DevConfig)
app.config.from_pyfile('config.py')

from app import views
