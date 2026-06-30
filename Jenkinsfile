pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Build Docker Image') {
            steps {
                sh 'docker build -f docker/Dockerfile -t app-devops .'
            }
        }
        stage('Deploy') {
            steps {
                sh '''
                    docker stop app-devops-container || true
                    docker rm app-devops-container || true
                    docker run -d -p 8082:8000 --name app-devops-container app-devops
                '''
            }
        }
    }
}
