pipeline {

    agent any
    stages {
        stage(build) {
            steps {
                script {
                    sh 'docker build -t GithubAPI .'
                }
            }

        }
        
    }
}