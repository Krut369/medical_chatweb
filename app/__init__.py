from flask import Flask
from .config import Config
from .routes import main_bp

def create_app():
    app = Flask(__name__)

    # Load config from config.py
    app.config.from_object(Config)

    # Register routes blueprint
    app.register_blueprint(main_bp)

    return app
