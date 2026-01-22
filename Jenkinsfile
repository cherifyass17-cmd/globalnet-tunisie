pipeline {
    agent any

    environment {
        DOCKER_HUB_USERNAME = 'yasminech123'
        DOCKER_HUB_CREDENTIALS_ID = 'docker-hub-credentials'
    }

    stages {

        stage('Build & Push Offers') {
            steps {
                script {
                    docker.build("${DOCKER_HUB_USERNAME}/offers-service:latest", "./offers")
                    docker.withRegistry('https://registry.hub.docker.com', DOCKER_HUB_CREDENTIALS_ID) {
                        docker.image("${DOCKER_HUB_USERNAME}/offers-service:latest").push()
                    }
                }
            }
        }

        stage('Build & Push Auth') {
            steps {
                script {
                    docker.build("${DOCKER_HUB_USERNAME}/auth-service:latest", "./auth")
                    docker.withRegistry('https://registry.hub.docker.com', DOCKER_HUB_CREDENTIALS_ID) {
                        docker.image("${DOCKER_HUB_USERNAME}/auth-service:latest").push()
                    }
                }
            }
        }

        stage('Build & Push Contact') {
            steps {
                script {
                    docker.build("${DOCKER_HUB_USERNAME}/contact-service:latest", "./contact")
                    docker.withRegistry('https://registry.hub.docker.com', DOCKER_HUB_CREDENTIALS_ID) {
                        docker.image("${DOCKER_HUB_USERNAME}/contact-service:latest").push()
                    }
                }
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                withCredentials([file(credentialsId: 'kubeconfig', variable: 'KUBECONFIG')]) {
                    sh '''
                        export KUBECONFIG=$KUBECONFIG
                        kubectl apply --validate=false -f k8s/
                    '''
                }
            }
        }
    }
}
