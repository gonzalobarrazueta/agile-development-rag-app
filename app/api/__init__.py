from flask import Flask


def create_app():
    app = Flask(__name__)

    # Import and register the routes
    #from .app import search_route, generate_route
    #app.register_blueprint(search_route, url_prefix='/api')
    #app.register_blueprint(generate_route, url_prefix='/api')

    @app.route('/')
    def index():
        return {"message": "Welcome to the API!"}

    return app
