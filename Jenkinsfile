pipeline {

    agent any

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build Backend Image') {
            steps {
                sh '''
                cd travel-booking
                docker build -t travel-backend ./backend
                '''
            }
        }

        stage('Build Frontend Image') {
            steps {
                sh '''
                cd travel-booking
                docker build -t travel-frontend .
                '''
            }
        }

        stage('Create Network') {
            steps {
                sh '''
                docker network create travel-network || true
                '''
            }
        }

        stage('Deploy Backend') {
            steps {
                sh '''
                docker rm -f travel-backend || true

                docker run -d \
                --name travel-backend \
                --network travel-network \
                -p 5000:5000 \
                -e DB_HOST=database-1.ctcmgywsktm4.ap-south-1.rds.amazonaws.com \
                -e DB_USER=admin \
                -e DB_PASSWORD=admin12345 \
                -e DB_NAME=travel_booking \
                travel-backend
                '''
            }
        }

        stage('Deploy Frontend') {
            steps {
                sh '''
                docker rm -f travel-frontend || true

                docker run -d \
                --name travel-frontend \
                --network travel-network \
                -p 80:80 \
                travel-frontend
                '''
            }
        }

        stage('Verify') {
            steps {
                sh '''
                docker ps
                curl -X POST http://localhost/book \
                -H "Content-Type: application/json" \
                -d '{"name":"Jenkins Test","email":"jenkins@test.com","phone":"9999999999"}'
                '''
            }
        }
    }
}
