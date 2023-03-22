from flask import Blueprint, jsonify

root_bp = Blueprint("root", __name__)


@root_bp.route("/", methods=["GET"])
def get_users():
    print("Hello World")
    return jsonify({"message": "Hello World"})
