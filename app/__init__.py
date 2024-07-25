from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from app.modules import hello, users, test
from app.database.postgres import db

from config import Config



def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    app.register_blueprint(url_prefix="/", blueprint=hello.blueprint)
    app.register_blueprint(url_prefix='/api/test', blueprint=test.blueprint)
    app.register_blueprint(url_prefix='/api/users', blueprint=users.blueprint)
    
    return app