from flask import Blueprint, render_template, current_app, request
from todoapp.extensions import assets, socketio
from flask_assets import Bundle
from flask_socketio import emit


js = Bundle(
    'https://cdnjs.cloudflare.com/ajax/libs/vue/2.1.8/vue.js',
    'https://cdnjs.cloudflare.com/ajax/libs/axios/0.15.3/axios.min.js',
    'js/infinite-scroll.js',
    'https://ajax.googleapis.com/ajax/libs/jquery/2.2.4/jquery.min.js',
    'js/notify.js',
    'https://cdn.jsdelivr.net/lodash/4.17.4/lodash.js',
    'https://cdnjs.cloudflare.com/ajax/libs/socket.io/1.7.2/socket.io.js',
    'js/app.js',
    filters='jsmin',
    output='gen/app.js'
)
assets.register(
    'jsall',
    js
)

css = Bundle(
    'css/app.css',
    'https://fonts.googleapis.com/css?family=Roboto:400,500,700',
    'https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.css',
    filters='cssmin',
    output='gen/app.css'
)

assets.register(
    'cssall',
    css
)

mybp = Blueprint(
    'frontedbp',
    __name__
)


@mybp.route('/')
def index():
    return render_template(
        'index.html'
    )


@socketio.on('connect')
def v():
    current_app.logger.info('New user connected with ip {ip}'
                            .format(ip=request.remote_addr))


@socketio.on('newtodo')
def newtodo(tododata):
    current_app.logger.info('New todo from {ip}'
                            .format(ip=request.remote_addr))
    emit('newtodo', tododata, broadcast=True, include_self=False)


@socketio.on('removetodo')
def removetodo(tododata):
    current_app.logger.info('Remove todo from {ip}'
                            .format(ip=request.remote_addr))
    emit('removetodo', tododata, broadcast=True, include_self=False)


@socketio.on('donetodo')
def donetodo(tododata):
    current_app.logger.info('New todo from {ip}'
                            .format(ip=request.remote_addr))
    emit('donetodo', tododata, broadcast=True, include_self=False)
