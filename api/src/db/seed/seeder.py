"""
https://gist.github.com/jbnunn/2d2a5bc04da2edc3a71bfdcd2dce9c75
This script populates a DynamoDB table with seed data. Add seeds into a JSON file, named the same as your table.
The file should contain data that matches your database schema.
[
    {
      "email": test-email-1,
      "name": "dog"
    },
    {
      "email": test-email-2,
      "name": "cat"
    },
    ...
Run the file:
$ python3 seeder.py --region-name us-west-2 --endpoint http://localhost:8000 --table users
Scan table items:
$ aws dynamodb scan --table-name users --endpoint-url http://localhost:8000
"""
import os
import argparse
import sys
import json
import boto3


class Seeder:

    def __init__(self, region_name="us-west-2", endpoint_url=None):
        """Initializes the Seeder class
        Pass `"http://localhost:8000"` for endpoint_url to run against localhost aka DynamoDB Local, 
        https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DynamoDBLocal.html)
        """
        self.dynamodb = boto3.resource(
            'dynamodb', region_name=region_name, endpoint_url=endpoint_url)

    def seed_table(self, table_name):
        """Imports data into a DynamoDB database
        Imports a seed file based on the same case-sensitive name, in `./<table>.json` (JSON-based), into an 
        existing database. If the seed key already exists, it is overwritten.
        Args:
            table: An existing DynamoDB database
        Returns:
            A dict of total_seeds found in the json file, number of successful writes, and
            number of failed writes, e.g.,
            {'total_seeds': 106, 'successful_writes': 106, 'failed_writes': 0}
        Raises:
            Exception: An error (usually ParamValidationError) if a parameter (i.e. column name) was 
            not found in the DDB table.
        """
        table = self.dynamodb.Table(table_name)
        basedir = os.path.abspath(os.path.dirname(__file__))
        with open((f"{basedir}/{table_name}.json")) as json_file:
            seeds = json.load(json_file)
            writes = 0
            fails = 0
            for seed in seeds:
                item = {}
                for k, v in seed.items():
                    item[k] = v
                try:
                    table.put_item(Item=item)
                    writes += 1
                except:
                    print(f"Error adding: {seed}, {sys.exc_info()[1]}")
                    fails += 1

        return {"total_seeds": len(seeds), "successful_writes": writes, "failed_writes": fails}


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Seed a DynamoDB table')
    parser.add_argument('--region', '-r', default='us-west-1',
                        help='The AWS region the DynamoDB table lives in')
    parser.add_argument('--table', '-t', required=True,
                        help='The table name, which should be the same as the JSON file from which you\'re importing')
    parser.add_argument('--endpoint', '-e', default=None,
                        help='The endpoint URL of DDB. Leave empty for cloud DDB, or specify `http://localhost:8000` for DynamoDB local')

    args = parser.parse_args()

    seeder = Seeder(args.region, args.endpoint)
    result = seeder.seed_table(args.table)
    print(result)
