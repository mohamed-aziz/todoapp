
MONGO_QUERY_BLACKLIST = ['$where']

MONGO_HOST = 'localhost'
MONGO_PORT = 27017

MONGO_DBNAME = 'todoapp_database'

URL_PREFIX = 'api'

API_VERSION = 'v1'


schema = {
    'todotext': {
        'type': 'string',
        'minlength': 4
    },
    'done': {
        'type': 'boolean',
        'default': False
    }
}

DOMAIN = {
    'todos': {
        'item_title': 'todo',
        'resource_methods': ['GET', 'POST'],
        'schema': schema,
        'item_methods': ['GET', 'PATCH', 'DELETE']
    }
}
