from flask import Flask


def create_app():
    app = Flask(__name__)

    from .routes.pages import pages
    app.register_blueprint(pages)

    return app