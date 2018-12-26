import os

from flask import Flask
from flasgger import Swagger
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from mongoengine import connect

from view import Router
from config.config import ConfigObject


def create_app():
    template_dir = os.path.abspath('../../Forest.FrontEnd/build')
    app = Flask(__name__, template_folder=template_dir)

    connect('localhost')

    app.config.from_object(ConfigObject)
    CORS(app)
    Router(app).register()
    JWTManager(app)
    Swagger(app, template=app.config['SWAGGER_TEMPLATE'])

    return app
