from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from app.modules import hello
from app.config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    # app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres'
    app.register_blueprint(hello.blueprint)
    return app