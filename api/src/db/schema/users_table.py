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
