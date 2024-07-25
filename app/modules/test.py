from flask import Blueprint
from flask import current_app

blueprint = Blueprint('test', __name__ )


@blueprint.route('/', methods=['GET'])
def hello():
    return f'Hello, {current_app.config.get("ENV_VAR")}!'