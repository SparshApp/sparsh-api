from flask import Flask
from flask_cors import CORS


def create_app():
    app = Flask(__name__)
    cors = CORS(app)

    from routes.routes import app_instance
    app.register_blueprint(app_instance)
    
    return app