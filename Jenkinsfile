pipeline {
    agent any
    
    environment {
        FLASK_APP = 'app.py'
        GUNICORN_CMD_ARGS = '--bind=0.0.0.0:8000  --workers=2 --timeout=60'
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
                sh 'pip install gunicorn'
                sh '. /var/lib/jenkins/workspace/Flask-app/benv/bin/activate && pip install gunicorn'
            }
        }
        
        stage('Unit tests') {
            steps {
                sh 'pytest test_app.py'
            }
        }
        
        stage('start flask app') {
            steps {
                sh '. /var/lib/jenkins/workspace/Flask-app/benv/bin/activate && flask run &'
            }
        } 
        
        stage('Deploy with Gunicorn') {
            steps {
                sh 'source /var/lib/jenkins/workspace/Flask-app/benv/bin/activate && gunicorn app:app &'
            }
        }
        
        stage ('post build') {
            steps {
                ansiblePlaybook credentialsId: 'JenkinsAns', installation: 'Ansible', inventory: '/var/lib/jenkins/workspace/Flask-app/inventory.ini', playbook: '/var/lib/jenkins/workspace/Flask-app/Hello.yml '
            }
        }
    }
}
