pipeline {

    agent none
    stages {
        stage(build) {
            step {
                script {
                    docker build -t GithubAPI .
                }
            }

        }
        
    }
}