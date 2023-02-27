from flask import Blueprint

app_instance = Blueprint(name="app_instance", import_name=__name__)

@app_instance.route("/")
def index():
    return "Hello World!"
