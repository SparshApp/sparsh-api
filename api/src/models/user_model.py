import uuid
import boto3
from botocore.exceptions import ClientError

dynamodb = boto3.resource('dynamodb',
                          endpoint_url='http://localhost:8000',
                          region_name='anywhere',
                          aws_access_key_id='who',
                          aws_secret_access_key='cares')
users_table = dynamodb.Table('users')
USERS_TABLE_SCHEMA = {
    'TableName': 'users',
    'KeySchema': [
        {
            'AttributeName': 'email',
            'KeyType': 'HASH'  # Partition key
        },
        {
            'AttributeName': 'name',
            'KeyType': 'RANGE'
        }
    ],
    'AttributeDefinitions': [
        {
            'AttributeName': 'email',
            'AttributeType': 'S'
        },
        {
            'AttributeName': 'name',
            'AttributeType': 'S'
        }
    ],
    'ProvisionedThroughput': {
        'ReadCapacityUnits': 5,
        'WriteCapacityUnits': 5
    }
}


def create_users_table():
    try:
        table = dynamodb.create_table(**USERS_TABLE_SCHEMA)
        table.wait_until_exists()
        return True
    except ClientError as e:
        # TODO: add logging and raise custom exception
        print(e)
        return False


def create_user(name, email):
    user_id = str(uuid.uuid4())
    user = User(user_id, name, email)
    # TODO: Save user data to the 'users' table
    return user


def get_user(user_id):
    user_data = None  # TODO: Retrieve user data from the 'users' table
    return User.from_dict(user_data)


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
