APP_NAME := sparsh-api
APP_IMAGE := $(APP_NAME):latest
APP_ENV ?= dev
AWS_REGION = us-west-2
AWS_ACCOUNT_ID = 1234567890
DOCKER_REGISTRY = $(AWS_ACCOUNT_ID).dkr.ecr.$(AWS_REGION).amazonaws.com/$(APP_NAME)

.PHONY: help
help:
	@echo "Available targets:"
	@echo "  help             - display this help message"
	@echo "  build            - build the Docker images"
	@echo "  unit-tests       - run unit tests"
	@echo "  integration 	  - run integration tests"
	@echo "  lint             - run lint checks"
	@echo "  coverage         - generate test coverage report"
	@echo "  run              - run the Flask app"
	@echo "  infra-deploy     - deploy infrastructure changes"
	@echo "  infra-destroy    - destroy infrastructure"
	@echo "  deploy           - deploy the Flask app"

build:
	docker-compose build

unit-test:
	docker run --rm $(APP_IMAGE) pytest api/tests/unit/

integration:
	docker run --rm $(APP_IMAGE) pytest api/tests/integration/

lint:
	docker run --rm $(APP_IMAGE) pylint api/

coverage:
	docker run --rm $(APP_IMAGE) pytest --cov=app api/tests/unit/
	docker run --rm $(APP_IMAGE) pytest --cov-report=html api/tests/unit/
	open htmlcov/index.html

run-local:
	@echo "Running local server"
	docker build api/src -t sparsh-api
	docker run --rm sparsh-api

seed-users-local:
	@echo "Seeding users table in local database"
	@echo "Make sure you have activated your virtual environment: 'source venv/bin/activate'"
	python3 api/src/db/seed/seeder.py --table users --endpoint http://localhost:8000

run-prod:
	@echo "Running production server"
	docker-compose down
	docker-compose build
	docker-compose up

# Push Docker images to AWS ECR
push-dev:
	docker tag sparsh-api-dev:latest aws_account_id.dkr.ecr.us-west-2.amazonaws.com/sparsh-api-dev:latest
	docker push aws_account_id.dkr.ecr.us-west-2.amazonaws.com/sparsh-api-dev:latest

push-qa:
	docker tag sparsh-api-qa:latest aws_account_id.dkr.ecr.us-west-2.amazonaws.com/sparsh-api-qa:latest
	docker push aws_account_id.dkr.ecr.us-west-2.amazonaws.com/sparsh-api-qa:latest

push-prod:
	docker tag sparsh-api-prod:latest aws_account_id.dkr.ecr.us-west-2.amazonaws.com/sparsh-api-prod:latest
	docker push aws_account_id.dkr.ecr.us-west-2.amazonaws.com/sparsh-api-prod:latest

# Deploy AWS infrastructure
infra-deploy:
	cd infra/scripts && sh deploy.sh

infra-destroy:
	cd infra/scripts && sh destroy.sh
