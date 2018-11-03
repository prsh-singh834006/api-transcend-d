from .main.controllers.user_controller import UserController
from flask_restplus import Api
from flask import Blueprint

blueprint = Blueprint('user_controller',__name__, url_prefix='/api')

api = Api(blueprint)
api.add_resource(UserController, '/show')