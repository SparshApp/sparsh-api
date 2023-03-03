import yaml

with open("config.yml", 'r') as ymlfile:
    config = yaml.load(ymlfile, Loader=yaml.FullLoader)

class Config:
    DEBUG = config['debug']
    TESTING = config['testing']
    SECRET_KEY = config['secret_key']
    SQLALCHEMY_DATABASE_URI = config['database_uri']
    SQLALCHEMY_TRACK_MODIFICATIONS = False
