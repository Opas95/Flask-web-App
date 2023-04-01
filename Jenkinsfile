pipeline {
    agent any
    
    environment {
        FLASK_APP = 'app.py'
      
    }
    
    stages {
        stage('Clone repository') {
            steps {
                git branch: 'main', url: 'https://github.com/Opas95/Flask-web-App.git'
            }
        }
        
        stage('Install dependencies') {
            steps {
                sh 'virtualenv benv'
                sh '. /var/lib/jenkins/workspace/Flask-app/benv/bin/activate && pip install flask'
            }
        }
        
        stage('Unit tests') {
            steps {
                sh 'pytest test_app.py'
            }
        }
        
        stage('Start Flask app') {
            steps {
                sh '. /var/lib/jenkins/workspace/Flask-app/benv/bin/activate && nohup flask run &'
            }
        }
        
        stage('Integration tests') {
            steps {
                sh 'python integration_test.py'
            }
        }
    }
}
