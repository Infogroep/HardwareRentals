from os.path import join, dirname, abspath

class Config(object):
    DEBUG = False
    TESTING = False
    ROOT = dirname(abspath(__file__))
    TEMPLATE = 'templates'
    SECRET_KEY = ''
    SERVER_NAME = None
    STATUS = 'Testing'
    SESSIONS = {
        'session.type' : 'memory',
        'session.auto' : True,
        'session.cookie_expires' : 600,
        'session.key' : 'LoggedIn',
        'session.secret' : 'SessionSecretKey'
    }
    DATABASE = 'hardware_rentals'
    DB_USER = 'hardware_rentals'
    DB_PASSWORD = ''

class ProductionConfig(Config):
    TEMPLATE = join(Config.ROOT,'static/templates')
    SECRET_KEY = """HahaBLortTesting"""
    SERVER_NAME = 'rentals.infogroep.be'
    STATUS = 'Production'

class DevelopmentConfig(Config):
    TEMPLATE = join(Config.ROOT,'static/templates')
    DEBUG = True
    SECRET_KEY = 'SECRET!'