

class Config:
    """Documentation for Config

    """
    SECRET_KEY = 'something-really-secret'
    MY_BLUEPRINTS = []


class devConfig(Config):
    ASSETS_DEBUG = True
    DEBUG = True
