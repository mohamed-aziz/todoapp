from flask_assets import Environment
from flask_socketio import SocketIO

assets = Environment()
socketio = SocketIO()

__all__ = [
    'assets', 'socketio'
]
