#!/bin/bash

fuser -k $1/tcp

export WORKON_HOME="/home/webuser/.virtualenvs"

source /usr/share/virtualenvwrapper/virtualenvwrapper.sh

echo "Running todoapp page app on port $1"

workon todoapp

cd /home/webuser/Projects/todoap

pip install -r requirements.txt

python manage.py assets build

gunicorn --worker-class=meinheld.gmeinheld.MeinheldWorker -b 127.0.0.1:$1 wsgi:app
