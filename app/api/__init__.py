from flask import Flask
from flask_cors import CORS


def create_app():
    app = Flask(__name__)

    CORS(app)

    from .app import generate_route
    app.register_blueprint(generate_route, url_prefix='/api')

    @app.route('/')
    def index():
        return {"message": "Welcome to the API!"}

    return app
