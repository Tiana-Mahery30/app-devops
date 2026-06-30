pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                echo 'Récupération du code depuis Git...'
            }
        }
        stage('Build Docker Image') {
            steps {
                echo 'Construction de l\'image Docker...'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Déploiement de l\'application...'
            }
        }
    }
}
