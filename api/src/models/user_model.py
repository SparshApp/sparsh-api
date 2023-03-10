from flask import current_app
import boto3
from boto3.dynamodb.conditions import Key
from botocore.exceptions import ClientError

dynamodb = boto3.resource('dynamodb', endpoint_url=current_app.config['DYNAMO_ENDPOINT_URL'])
users_table = dynamodb.Table('users')


class User:
    def __init__(self, id, name, email):
        self.id = id
        self.name = name
        self.email = email

    def save(self):
        try:
            users_table.put_item(Item={
                'id': self.id,
                'name': self.name,
                'email': self.email
            })
        except ClientError as e:
            print(e.response['Error']['Message'])

    def delete(self):
        try:
            users_table.delete_item(Key={'id': self.id})
        except ClientError as e:
            print(e.response['Error']['Message'])

    @classmethod
    def get_all(cls):
        try:
            response = users_table.scan()
            items = response.get('Items', [])
            users = [User(item['id'], item['name'], item['email'])
                     for item in items]
            return users
        except ClientError as e:
            print(e.response['Error']['Message'])

    @classmethod
    def get_by_id(cls, id):
        try:
            response = users_table.query(
                KeyConditionExpression=Key('id').eq(id))
            items = response.get('Items', [])
            if len(items) == 0:
                return None
            item = items[0]
            user = User(item['id'], item['name'], item['email'])
            return user
        except ClientError as e:
            print(e.response['Error']['Message'])
