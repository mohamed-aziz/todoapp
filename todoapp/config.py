

class Config:
    """Documentation for Config

    """
    SECRET_KEY = 'something-really-secret'
    MY_BLUEPRINTS = []


class devConfig(Config):
    ASSETS_DEBUG = True
    DEBUG = True


class prodConfig(Config):
    # just to make sure when an idiot messes with
    # our Config class
    ASSETS_DEBUG = False
    DEBUG = True
