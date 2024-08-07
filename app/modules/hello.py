from flask import Blueprint
from flask import current_app

blueprint = Blueprint('hello', __name__)


@blueprint.route('/', methods=['GET'])
def hello():
    return f'Home, {current_app.config.get("ENV_VAR")}!'