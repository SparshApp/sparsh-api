import os
import yaml
from .secrets import Secrets
from db.schema import USERS_TABLE_SCHEMA

env = os.getenv('APP_ENV', 'dev')
secrets = Secrets()

def parse_config_yaml():
    basedir = os.path.abspath(os.path.dirname(__file__))
    with open(basedir + '/../config.yml') as f:
        config = yaml.safe_load(f)
    return config[env]


class BaseConfig:
    DEBUG = False
    DEVELOPMENT = True
    TESTING = False
    CSRF_ENABLED = True

    # TODO: add default values
    AWS_ACCESS_KEY_ID = parse_config_yaml().get('aws').get('access_key_id')
    AWS_SECRET_ACCESS_KEY = secrets.get_secrets().get('AWS_SECRET_ACCESS_KEY')
    AWS_REGION = parse_config_yaml().get('aws').get('region')

    DYNAMO_TABLES = [
        USERS_TABLE_SCHEMA
    ]
    DYNAMO_ENDPOINT_URL = parse_config_yaml().get('dynamo').get('endpoint_url')
    DYNAMO_ENABLE_LOCAL = parse_config_yaml().get('dynamo').get('enable_local')
    DYNAMO_LOCAL_HOST = parse_config_yaml().get('dynamo').get('local_host')
    DYNAMO_LOCAL_PORT = parse_config_yaml().get('dynamo').get('local_port')


class TestingConfig(BaseConfig):
    TESTING = True


class DevelopmentConfig(BaseConfig):
    DEBUG = True


class QAConfig(BaseConfig):
    DEBUG = True


class ProductionConfig(BaseConfig):
    DEVELOPMENT = False


config_by_name = dict(
    test=TestingConfig,
    dev=DevelopmentConfig,
    qa=QAConfig,
    prod=ProductionConfig
)
