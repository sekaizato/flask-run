from flask import Blueprint, jsonify, request

from app.models.user import User
from app.utils.sql import to_dict

from app.database.postgres import db

blueprint = Blueprint('users', __name__ )


@blueprint.route('/', methods=['GET'])
def list_users():
    users = User.query.all()
    users_list = [to_dict(user) for user in users]
    return jsonify({"data":users_list}), 200


@blueprint.route('/', methods=['POST'])
def add_user():
    data = request.get_json()
    if not data or not 'username' in data or not 'email' in data:
        return jsonify({"error": "Invalid input"}), 400
    
    username = data['username']
    email = data['email']

    # Check for existing username
    if User.query.filter_by(username=username).first():
        return jsonify({"error": "Username already exists"}), 409

    # Check for existing email
    if User.query.filter_by(email=email).first():
        return jsonify({"error": "Email already exists"}), 409
    
    new_user = User(username=username, email=email)
    db.session.add(new_user)
    db.session.commit()
    
    return jsonify({"message": "User added successfully", "user": to_dict(new_user)}), 201


@blueprint.route('/<id>', methods=['GET'])
def get_user(id):
    user = User.query.get(id)
    if not user:
        return jsonify({"error": "User not found"}), 404
    return jsonify(to_dict(user)), 200


@blueprint.route('/<id>', methods=['DELETE'])
def delete_user(id):
    user = User.query.get(id)
    if not user:
        return jsonify({"error": "User not found"}), 404
    db.session.delete(user)
    db.session.commit()
    return jsonify({"message": "User deleted successfully", "user": to_dict(user)}), 200


@blueprint.route('/<id>', methods=['PUT'])
def update_user(id):
    user = User.query.get(id)
    if not user:
        return jsonify({"error": "User not found"}), 404
    
    data = request.get_json()
    if not data:
        return jsonify({"error": "Invalid input"}), 400

    if 'username' in data:
        if User.query.filter_by(username=data['username']).first() and data['username'] != user.username:
            return jsonify({"error": "Username already exists"}), 409
        user.username = data['username']
    
    if 'email' in data:
        if User.query.filter_by(email=data['email']).first() and data['email'] != user.email:
            return jsonify({"error": "Email already exists"}), 409
        user.email = data['email']
    
    db.session.commit()
    return jsonify({"message": "User updated successfully", "user": to_dict(user)}), 200