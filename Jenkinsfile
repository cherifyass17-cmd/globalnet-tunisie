pipeline {
    agent any

    environment {
        DOCKER_HUB_USERNAME = 'yasminech123'
        DOCKER_HUB_CREDENTIALS_ID = 'docker-hub-credentials'
        KUBECONFIG_CREDENTIALS_ID = 'kubeconfig'
    }

    stages {
        stage('Build & Push Offers') {
            steps {
                script {
                    docker.build("${env.DOCKER_HUB_USERNAME}/offers-service:latest", "./offers")
                    docker.withRegistry('https://registry.hub.docker.com', env.DOCKER_HUB_CREDENTIALS_ID) {
                        docker.image("${env.DOCKER_HUB_USERNAME}/offers-service:latest").push()
                    }
                }
            }
        }

        stage('Build & Push Auth') {
            steps {
                script {
                    docker.build("${env.DOCKER_HUB_USERNAME}/auth-service:latest", "./auth")
                    docker.withRegistry('https://registry.hub.docker.com', env.DOCKER_HUB_CREDENTIALS_ID) {
                        docker.image("${env.DOCKER_HUB_USERNAME}/auth-service:latest").push()
                    }
                }
            }
        }

        stage('Build & Push Contact') {
            steps {
                script {
                    docker.build("${env.DOCKER_HUB_USERNAME}/contact-service:latest", "./contact")
                    docker.withRegistry('https://registry.hub.docker.com', env.DOCKER_HUB_CREDENTIALS_ID) {
                        docker.image("${env.DOCKER_HUB_USERNAME}/contact-service:latest").push()
                    }
                }
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                withCredentials([string(credentialsId: env.KUBECONFIG_CREDENTIALS_ID, variable: 'KUBECONFIG_CONTENT')]) {
                    sh '''
                        mkdir -p ~/.kube
                        echo "$KUBECONFIG_CONTENT" > ~/.kube/config
                        chmod 600 ~/.kube/config
                        kubectl apply --validate=false -f k8s/
                    '''
                }
            }
        }
    }
}
