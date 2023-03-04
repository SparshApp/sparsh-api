# https://savelev.medium.com/best-practice-how-to-store-secrets-and-settings-in-python-project-e3ee45b3094c

import os
import json
import boto3
from botocore.exceptions import ClientError


def get_secrets(self) -> dict:
    return self.from_json() or self.from_aws('<secrets-name>')


def get_secrets_from_json(self) -> dict:
    filename = os.path.join('secrets.json')
    try:
        with open(filename, mode='r') as f:
            return json.loads(f.read())
    except FileNotFoundError:
        return {}


def get_secrets_from_aws(secret_name: str) -> dict:
    region_name = os.environ['AWS_REGION']
    session = boto3.session.Session()
    client = session.client(
        service_name='secretsmanager', region_name=region_name)
    try:
        get_secret_value_response = client.get_secret_value(
            SecretId=secret_name)
    except ClientError as e:
        print(e.response['Error']['Code'])
        return {}
    else:
        if 'SecretString' in get_secret_value_response:
            secret = get_secret_value_response['SecretString']
            secret = json.loads(secret)
            return secret
