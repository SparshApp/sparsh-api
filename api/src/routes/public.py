from flask import Blueprint, jsonify

app_bp = Blueprint("app", __name__)


@app_bp.route("/", methods=["GET"])
def get_users():
    print("Hello World")
    return jsonify({"message": "Hello World"})
