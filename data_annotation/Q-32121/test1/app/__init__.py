from flask import Flask
from .pages import pages_bp

def create_app():
    app = Flask(__name__)
    app.register_blueprint(pages_bp)
    return app