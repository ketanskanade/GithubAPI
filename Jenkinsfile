pipeline {

    agent any
    stages {
        stage(build) {
            steps {
                script {
                    docker.build(git@github.com:ketanskanade/GithubAPI.git/GithubAPI)
                }
            }

        }
        
    }
}