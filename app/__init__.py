from flask import Flask
from config import config


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    from app.admin import admin

    app.register_blueprint(admin)

    from app.usr import usr

    app.register_blueprint(usr)

    return app