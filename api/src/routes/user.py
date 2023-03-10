from flask import Blueprint, jsonify, request
from models import user_model

users_bp = Blueprint("users", __name__, url_prefix="/users")


@users_bp.route("", methods=["GET"])
def get_users():
    users = user_model.User.get_all()
    return jsonify([user.__dict__ for user in users])


@users_bp.route("/<user_id>", methods=["GET"])
def get_user(user_id):
    user = user_model.User.get_by_id(user_id)
    if not user:
        return jsonify({"error": "User not found"}), 404
    return jsonify(user.__dict__)


@users_bp.route("", methods=["POST"])
def create_user():
    data = request.get_json()
    if not data:
        return jsonify({"error": "Invalid input data"}), 400
    user = user_model.User(data.get("id"), data.get("name"), data.get("email"))
    user.save()
    return jsonify(user.__dict__), 201


@users_bp.route("/<user_id>", methods=["DELETE"])
def delete_user(user_id):
    user = user_model.User.get_by_id(user_id)
    if not user:
        return jsonify({"error": "User not found"}), 404
    user.delete()
    return "", 204
