pipeline {
    agent any
    environment {
        APP_ENV = ''
        AWS_REGION = 'us-west-2'
        AWS_ACCOUNT_ID = '1234567890'
        AWS_ACCESS_KEY_ID = credentials('aws-access-key-id')
        AWS_SECRET_ACCESS_KEY = credentials('aws-secret-access-key')
        DOCKER_REGISTRY = "${AWS_ACCOUNT_ID}.dkr.ecr.${AWS_REGION}.amazonaws.com"
    }
    stages {
        stage('Checkout') {
            steps {
                checkout([
                    $class: 'GitSCM',
                    branches: [[name: '*/main']],
                    userRemoteConfigs: [[url: 'https://github.com/SparshApp/sparsh-api.git']]
                ])
            }
        }
        stage('Build') {
            steps {
                sh 'make build'
            }
        }
        stage('Unit Tests') {
            steps {
                sh 'make unit-tests'
            }
        }
        stage('Static Analysis') {
            steps {
                sh 'make lint'
            }
        }
        stage('Coverage') {
            steps {
                sh 'make coverage'
            }
        }
        stage('Deploy to Dev') {
            environment {
                APP_ENV = 'dev'
            }
            parallel {
                stage('Integration Tests') {
                    steps {
                        sh 'make integration-tests'
                    }
                }
                stage('End-to-End Tests') {
                    steps {
                        sh 'make e2e-tests'
                    }
                }
            }
            stage('Deploy App') {
                steps {
                    sh 'make run-prod'
                }
            }
        }
        stage('Deploy to QA') {
            environment {
                APP_ENV = 'qa'
            }
            parallel {
                stage('Integration Tests') {
                    steps {
                        sh 'make integration-tests'
                    }
                }
                stage('End-to-End Tests') {
                    steps {
                        sh 'make e2e-tests'
                    }
                }
            }
            stage('Deploy App') {
                steps {
                    sh 'make run-prod'
                }
            }
        }
        stage('Deploy to Prod') {
            environment {
                APP_ENV = 'prod'
            }
            stage('Deploy App') {
                steps {
                    sh 'make run-prod'
                }
            }
        }
        stage('Push to ECR') {
            steps {
                withCredentials([[
                    $class: 'AmazonWebServicesCredentialsBinding',
                    accessKeyVariable: 'AWS_ACCESS_KEY_ID',
                    credentialsId: 'aws-creds',
                    secretKeyVariable: 'AWS_SECRET_ACCESS_KEY'
                ]]) {
                    sh 'make push-to-ecr'
                }
            }
        }
    }
}
