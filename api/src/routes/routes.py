from flask import Blueprint

app_bp = Blueprint(name="sparsh_api", import_name=__name__)


@app_bp.route("/")
def index():
    return "Hello World!"


@app_bp.route("/login")
def login():
    return "Login!"
