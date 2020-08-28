import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    SECRET_KEY = 'this-is-a-secret-key'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(object):
	DEBUG  = False

class TestingConfig(object):
	TESTING = True
	DEBUG = True

class ProductionConfig(object):
	DEBUG = False


class DevelopmentConfig(object):
	DEVELOPMENT = True
	DEBUG = True