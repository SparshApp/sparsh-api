from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

# Create a SQLAlchemy instance
db = SQLAlchemy()

def create_db(app):
    db.init_app(app)
    db.create_all(app=app)

def create_app():
    app = Flask(__name__)
    CORS(app)

    from routes.routes import app_instance
    app.register_blueprint(app_instance)

    create_db(app)
    
    return app