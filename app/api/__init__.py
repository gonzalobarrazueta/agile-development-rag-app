from flask import Flask


def create_app():
    app = Flask(__name__)

    from .app import generate_route

    app.register_blueprint(generate_route, url_prefix='/api')

    @app.route('/')
    def index():
        return {"message": "Welcome to the API!"}

    return app
