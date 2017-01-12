from eve import Eve
from .extensions import assets
from .frontend import frontedbp


def create_app(config):
    # create the app

    app = Eve(__name__)
    app.config.from_object(config)
    register_extensions(app)
    register_blueprints(app)

    return app


def register_extensions(app):
    # create the bundle and register it to the assets
    assets.init_app(app)


def register_blueprints(app):
    app.register_blueprint(
        frontedbp
    )
