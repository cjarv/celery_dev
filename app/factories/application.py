from flask import Flask
from app.config import DevConfig
from controllers import home


def create_application(config=DevConfig):
    app = Flask(__name__)
    app.config.from_object(config)
    app.register_blueprint(home)
    return app
