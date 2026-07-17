pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build') {
            steps {
                echo "Building travel booking assistant"
            }
        }

        stage('Test') {
            steps {
                echo "Running tests"
            }
        }
    }
}
