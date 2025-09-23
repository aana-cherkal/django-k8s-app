pipeline {
    agent any
    environment {
        DOCKER_HUB_CREDENTIALS = credentials('docker-hub-creds')
    }
    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/aana-cherkal/jenkins-ci-cd.git'
            }
        }
        stage('Build') {
            steps {
                sh 'docker build -t my-django-app .'
            }
        }
        stage('Test') {
            steps {
                sh 'docker run --rm my-django-app python manage.py test'
            }
        }
        stage('Push to Docker Hub') {
            steps {
                sh '''
                echo $DOCKER_HUB_CREDENTIALS_PSW | docker login -u $DOCKER_HUB_CREDENTIALS_USR --password-stdin
                docker tag my-django-app aana-cherkal/my-django-app:latest
                docker push aana-cherkal/my-django-app:latest
                '''
            }
        }
    }
}
