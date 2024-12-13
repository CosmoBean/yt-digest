from flask import Flask


def create_app():
    # Create Flask app instance
    app = Flask(__name__)

    # Load configurations
    app.config.from_object("config.Config")

    from app.routes import app_routes
    app.register_blueprint(app_routes)

    return app
