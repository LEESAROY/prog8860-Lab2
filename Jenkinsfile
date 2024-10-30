pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build') {
            steps {
                echo 'starting build process'
                bat 'python -m pip install --upgrade pip'
            }
        }

        stage('Test') {
            steps {
                echo 'test started'
                bat 'python -m unittest test_app.py'
            }
        }
    }

    post {
        always {
            mail to: 'meleesa007@gmail.com',
                 subject: "Jenkins Build Notification: ${currentBuild.fullDisplayName}",
                 body: """\
                 Build Status: ${currentBuild.currentResult}
                 """
        }
    }
}
