from flask import Blueprint, jsonify

from app.models.user import User
# from app.database import to_dict
from app.utils.sql import to_dict

blueprint = Blueprint('users', __name__ )


@blueprint.route('/', methods=['GET'])
def list_users():
    users = User.query.all()
    users_list = [to_dict(user) for user in users]
    return jsonify({"data":users_list}), 200
