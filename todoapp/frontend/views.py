from flask import Blueprint, render_template
from todoapp.extensions import assets
from flask_assets import Bundle


js = Bundle(
    'https://cdnjs.cloudflare.com/ajax/libs/vue/2.1.8/vue.js',
    'https://cdnjs.cloudflare.com/ajax/libs/axios/0.15.3/axios.min.js',
    'js/infinite-scroll.js',
    'https://cdn.jsdelivr.net/lodash/4.17.4/lodash.js',
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
