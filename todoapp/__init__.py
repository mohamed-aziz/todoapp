from eve import Eve
from .extensions import assets, socketio
from .frontend import frontedbp
import os


def create_app(config):
    # create the app

    app = Eve(__name__, settings=os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'settings.py'))
    app.config.from_object(config)
    register_extensions(app)
    register_blueprints(app)

    return app


def register_extensions(app):
    # create the bundle and register it to the assets
    assets.init_app(app)
    socketio.init_app(app)

def register_blueprints(app):
    app.register_blueprint(
        frontedbp
    )
