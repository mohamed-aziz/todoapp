from flask import Blueprint, render_template
from todoapp.extensions import assets
from flask_assets import Bundle


js = Bundle(
    'https://unpkg.com/axios/dist/axios.min.js',
    'https://unpkg.com/vue-infinite-scroll@2.0.0',
    'https://cdn.jsdelivr.net/lodash/4.17.4/lodash.js',
    'js/app.js',
    # 'node_modules/vue-infinite-scroll/vue-infinite-scroll.js',
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
