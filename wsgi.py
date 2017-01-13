from todoapp import create_app
from todoapp.config import prodConfig

app = create_app(prodConfig)
