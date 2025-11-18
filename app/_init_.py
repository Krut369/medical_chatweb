from flask import Flask
from .config import Config
from .routes import main_bp

def create_app():
    app = Flask(_name_)
    app.config.from_object(Config)
    app.register_blueprint(main_bp)
    return app
