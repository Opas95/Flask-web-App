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
        
        stage('Build & start flask') {
            steps {
                sh '. /var/lib/jenkins/workspace/Flask-app/benv/bin/activate && nohup flask run --host=0.0.0.0 &'
                sh 'sleep 5s' // wait for Flask app to start up
                sh 'curl http://44.203.101.23:5000' // display contents of app.py
            }
        }
        
        stage('JaCoCo') {
            steps {
                jacoco()
            }
        }
        
        stage('slack notification') {
            steps {
                slackSend message: 'This application has passed the unit test. @manager please kindly approve app deployment'
            }
        }
        
        stage('Manager Approval Required.') {
            steps {
                echo "Taking approval from Manager before QA Deployment"
                timeout(time: 1, unit: 'DAYS') {
                    input message: 'Do you want to deploy this application?', submitter: 'admin'
                }
            }
        }
        
        stage('deployment') {
            steps {
                ansiblePlaybook credentialsId: 'private-key', disableHostKeyChecking: true, installation: 'Ansible', inventory: 'dev.ini', playbook: 'Hello.yml'
            }
        }
        
        stage('slack notification') {
            steps {
                slackSend message: 'flask app has been successfully deployed to prod'
            }
        }
    }
}
