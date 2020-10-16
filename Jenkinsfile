pipeline {
    agent { docker { image 'python:3.5.1' } }
    stages {
        stage('Test') {
            steps {
                sh 'cd tests'
                sh  'pytest --browser_name firefox'
            }
        }
    }
}