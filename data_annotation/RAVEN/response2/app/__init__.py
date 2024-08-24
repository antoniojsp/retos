# app/__init__.py
from flask import Flask


def create_app():
    app = Flask(__name__)
    app.config.update(
        TESTING=True,
        SECRET_KEY='192b9bdd22ab9ed4d12e236c78afcb9a393ec15f71bbf5dc987d54727823bcbf'
    )
    from . import routes
    app.register_blueprint(routes.bp)

    return app