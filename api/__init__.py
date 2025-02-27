import os

from flask import Flask
from flask_migrate import Migrate
from flask_cors import CORS
from flask.json import jsonify

import api.database.DBConnection as DBConn
from isiflask_core.app.Exceptions.APIException import APIException

MICROSERVICE_NAME = "core-services"

def create_app():
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_pyfile(os.path.abspath('./Environment.py'))
    app.config['SQLALCHEMY_DATABASE_URI'] = DBConn.connect_url
    app.config['MAX_CONTENT_LENGTH'] = 150 * 1000 * 1000
    app.url_map.strict_slashes = False
    migrate = Migrate(app, DBConn.db, render_as_batch=True)

    @migrate.configure
    def configure_alembic(config):
        # modify config object
        return config

    DBConn.db.init_app(app)
    CORS(app)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.errorhandler(APIException)
    def handle_invalid_usage(error: APIException):
        response = jsonify(error.to_dict())
        response.status_code = error.status_code
        return response
    
    @app.route('/')
    def home():
        return 'Hello World'

    from .routes import user_router
    app.register_blueprint(user_router, url_prefix=f'/api/{MICROSERVICE_NAME}/user')

    from .routes import p2ptransaction_router
    app.register_blueprint(p2ptransaction_router, url_prefix=f'/api/{MICROSERVICE_NAME}/p2ptransaction')

    return app
