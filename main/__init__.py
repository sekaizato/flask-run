from flask import Flask
from main.modules import hello
from main.config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    app.register_blueprint(hello.blueprint)
    return app