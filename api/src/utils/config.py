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

    AWS_ACCESS_KEY_ID = parse_config_yaml()['aws']['access_key_id']
    AWS_SECRET_ACCESS_KEY = secrets.get_secrets()['AWS_SECRET_ACCESS_KEY']
    AWS_REGION = parse_config_yaml()['aws']['region']

    DYNAMO_TABLES = [
        USERS_TABLE_SCHEMA
    ]
    DYNAMO_ENDPOINT_URL = parse_config_yaml()['dynamo']['endpoint_url']


class TestingConfig(BaseConfig):
    TESTING = True

    DYNAMO_ENABLE_LOCAL = parse_config_yaml()['dynamo']['enable_local']
    DYNAMO_LOCAL_HOST = parse_config_yaml()['dynamo']['local_host']
    DYNAMO_LOCAL_PORT = parse_config_yaml()['dynamo']['local_port']


class DevelopmentConfig(BaseConfig):
    DEBUG = True

    DYNAMO_ENABLE_LOCAL = parse_config_yaml()['dynamo']['enable_local']
    DYNAMO_LOCAL_HOST = parse_config_yaml()['dynamo']['local_host']
    DYNAMO_LOCAL_PORT = parse_config_yaml()['dynamo']['local_port']


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
