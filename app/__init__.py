from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import config

db = SQLAlchemy()
migrate = Migrate()

def create_app(config_obj):
    app = Flask(__name__)
    app.config.from_object(config[config_obj])
    db.init_app(app)
    migrate.init_app(app, db)

    # registering the api blueprint
    from .api import api as api_blueprint
    app.register_blueprint(api_blueprint, url_prefix="/api/v1")

    return app

