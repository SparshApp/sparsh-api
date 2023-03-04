import os
import yaml

env = os.environ.get('APP_ENV', 'dev')


def load_config():
    if env == 'prod':
        return ProdConfig
    elif env == 'qa':
        return QAConfig
    elif env == 'dev':
        return DevConfig
    elif env == 'test':
        return TestConfig
    else:
        # TODO: add logging and raise custom exception
        raise Exception('Invalid environment')


def parse_config_yaml():
    basedir = os.path.abspath(os.path.dirname(__file__))
    with open(basedir + '/../config.yml') as f:
        config = yaml.safe_load(f)
    return config[env]


class Config:
    DEBUG = False
    DEVELOPMENT = True
    TESTING = False
    CSRF_ENABLED = True
    SQLALCHEMY_DATABASE_URI = parse_config_yaml()['database']['db_uri']
    AWS_SECRET_KEY = parse_config_yaml()['aws']['secret_key']
    AWS_SECRET_NAME = parse_config_yaml()['aws']['secret_name']
    AWS_REGION = parse_config_yaml()['aws']['region']


class TestConfig(Config):
    TESTING = True


class DevConfig(Config):
    DEBUG = True


class QAConfig(Config):
    DEBUG = True


class ProdConfig(Config):
    DEVELOPMENT = False
