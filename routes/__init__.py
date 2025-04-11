from flask import Flask
from routes.main import main_bp

def register_blueprints(app: Flask):
    """
    NOTE: This function is used to register all blueprints in the application.
    """
    app.register_blueprint(main_bp)