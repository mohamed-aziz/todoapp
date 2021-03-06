from flask_script import Manager
from todoapp.config import devConfig
from todoapp import create_app
from todoapp.extensions import assets
from flask_assets import ManageAssets


app = create_app(devConfig)

manager = Manager(app)
manager.add_command("assets", ManageAssets(assets))


@manager.command
def socketserve():
    from todoapp.extensions import socketio
    socketio.run(app)


if __name__ == '__main__':
    manager.run()
