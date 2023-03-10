# Sparsh API

TODOs:

- Explore if secrets.json and secrets.json.template can be removed for the API. Update api to use AWS Secrets Manager or Docker secrets to get all secrets, and then update secrets.json and .env files to either be removed or ignored using .dockerignore

- Only allow requests from the API Gateway through, check for some AWS Gateway credential in the request headers. Create an auth middleware to check each of the requests

## Setup

1. `git clone git@github.com:SparshApp/sparsh-api.git`

1. `python3 -m venv venv`

1. `source venv/bin/activate`
