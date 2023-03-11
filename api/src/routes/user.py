from flask import Blueprint, jsonify, request
from services import UserService

users_bp = Blueprint("users", __name__, url_prefix="/users")

user_service = UserService()


@users_bp.route("", methods=["GET"])
def get_users():
    users = user_service.get_users()
    if not users:
        return jsonify({"error": "No users found"}), 404
    return jsonify([user.__dict__ for user in users])


@users_bp.route("/<user_id>", methods=["GET"])
def get_user(user_id):
    user = user_service.get_user(user_id)
    if not user:
        return jsonify({"error": "User not found"}), 404
    return jsonify(user.__dict__)


@users_bp.route("", methods=["POST"])
def create_user():
    data = request.get_json()
    if not data:
        return jsonify({"error": "Invalid input data"}), 400
    user = user_service.create_user(data.get("name"), data.get("email"))
    return jsonify(user.__dict__), 201


@users_bp.route("/<user_id>", methods=["DELETE"])
def delete_user(user_id):
    user = user_service.get_user(user_id)
    if not user:
        return jsonify({"error": "User not found"}), 404
    user.delete()
    return "", 204
