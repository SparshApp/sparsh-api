import os
from flask import Flask
from dotenv import load_dotenv
from flask_cors import CORS
from flask_login import LoginManager
from flask_dynamo import Dynamo
from flask_bcrypt import Bcrypt


# instantiate the extensions
dynamodb = Dynamo()
bcrypt = Bcrypt()
login_manager = LoginManager()


def create_app():
    # Instantiate the application
    app = Flask(__name__)

    # Enable CORS
    CORS(app, supports_credentials=True)

    # Load environment variables
    load_dotenv()

    # Configure the application
    from utils.config import config_by_name
    config = config_by_name[os.getenv('APP_ENV')]

    print(config)
    print(vars(config))

    app.config.from_object(config)

    # Set up extensions
    bcrypt.init_app(app)
    login_manager.init_app(app)
    dynamodb.init_app(app)
    with app.app_context():
        dynamodb.create_all()

    # Register route blueprints
    from routes import users_bp, app_bp
    app.register_blueprint(users_bp)
    app.register_blueprint(app_bp)

    return app

app = create_app()


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
