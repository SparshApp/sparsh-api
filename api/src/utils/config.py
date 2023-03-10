import os
import yaml
from .secrets import Secrets

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
    
    # AWS_SECRET_NAME = parse_config_yaml()['aws']['secret_name']
    # AWS_SECRETS = get_secrets_from_aws(AWS_SECRET_NAME)

    # DYNAMO_TABLES = [
    #     {
    #         'TableName': 'users',
    #         'KeySchema': [dict(AttributeName='username', KeyType='HASH')],
    #         'AttributeDefinitions':[dict(AttributeName='username', AttributeType='S')],
    #         'ProvisionedThroughput':dict(ReadCapacityUnits=5, WriteCapacityUnits=5)
    #     }
    # ]


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
