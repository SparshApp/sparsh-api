pipeline {
    agent {
        docker {
            image 'python:3.9.2-alpine3.13'
            args '-u root'
        }
    }

    environment {
        APP_NAME = 'my-app'
        DEV_ENV = 'dev'
        PROD_ENV = 'prod'
        DOCKER_REPO = 'my-docker-repo'
    }

    stages {
        stage('Build') {
            steps {
                sh 'pip install --upgrade pip'
                sh 'pip install -r requirements.txt'
                sh 'python -m compileall .'
                sh 'docker build -t ${DOCKER_REPO}/${APP_NAME}:${BUILD_NUMBER} .'
            }
        }

        stage('Lint') {
            steps {
                sh 'pip install pylint'
                sh 'find . -iname "*.py" | xargs pylint'
            }
        }

        stage('Unit Test') {
            steps {
                sh 'pip install pytest'
                sh 'pytest -v'
            }
        }

        stage('Integration Test') {
            when {
                environment name: 'BRANCH_NAME', value: 'dev'
            }
            steps {
                sh 'pip install pytest'
                sh 'pytest --env=${DEV_ENV} --integration'
            }
        }

        stage('Deploy') {
            when {
                environment name: 'BRANCH_NAME', value: 'master'
            }
            steps {
                withCredentials([usernamePassword(credentialsId: 'DOCKERHUB_CREDENTIALS', usernameVariable: 'DOCKER_USERNAME', passwordVariable: 'DOCKER_PASSWORD')]) {
                    sh 'docker login -u ${DOCKER_USERNAME} -p ${DOCKER_PASSWORD}'
                }
                sh 'docker push ${DOCKER_REPO}/${APP_NAME}:${BUILD_NUMBER}'
                sh 'kubectl set image deployment/${APP_NAME} ${APP_NAME}=${DOCKER_REPO}/${APP_NAME}:${BUILD_NUMBER} --namespace=${PROD_ENV}'
            }
        }
    }
}
