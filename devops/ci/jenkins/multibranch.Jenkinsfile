pipeline {
  agent { docker { image 'node:22' } }
  stages {
    stage('Install') { steps { sh 'npm ci' } }
    stage('Test')    { steps { sh 'npm test' } }
    stage('Deploy') {
      when { not { branch 'main' } }
      steps { echo "Deploying branch ${env.BRANCH_NAME} to review env" }
    }
  }
}
