from flask import Blueprint
from api.app.Controllers.UserController import index, find, store, update, delete
from api.app.Services.UserService import UserService

user_router = Blueprint('user', __name__)
user_service = UserService()

user_router.route('/', methods=['GET'], defaults={'service': user_service}) (index)
user_router.route('/', methods=['POST'], defaults={'service': user_service}) (store)
user_router.route('/<id>', methods=['GET'], defaults={'service': user_service}) (find)
user_router.route('/<id>', methods=['PUT'], defaults={'service': user_service}) (update)
user_router.route('/<id>', methods=['DELETE'], defaults={'service': user_service}) (delete)