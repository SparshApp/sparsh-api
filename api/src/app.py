from flask import Flask
from flask_cors import CORS
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
from routes.routes import app_bp
from utils.config import load_config

app = Flask(__name__)
CORS(app, supports_credentials=True)  # Enable CORS

load_dotenv()  # Load environment variables
config = load_config()
app.config.from_object(config)
app.secret_key = config.AWS_SECRET_KEY

# Init Flask LoginManager
login_manager = LoginManager(app)
login_manager.init_app(app)

# Create a SQLAlchemy instance
db = SQLAlchemy()
db.init_app(app)
# with app.app_context():
#     db.create_all()

# Register the routes
app.register_blueprint(app_bp)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
