'''
Config file for app
'''

class Config(object):
    SECRET_KEY = 'JKFNSOFBNSFBNLSIBNPGFWBJNGFPJWBNWP08930NWBOFDN33FBNS'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProdConfig(Config):
    SQLALCHEMY_URI = 'sqlite:///database.db'
    DEBUG = False


class DevConfig(Config):
    SQLALCHEMY_URI = 'sqlite:///database.db'
    DEBUG = False
    CACHE_TYPE = 'simple'
    ASSETS_DEBUG = True
    CELERY_BROKER_URL = 'amqp://guest:guest@localhost:15672//'
    CELERY_BACKEND_URL = 'rpc://'
