// vars/standardPipeline.groovy -- shared library entry point.
def call(Map config = [:]) {
  pipeline {
    agent any
    stages {
      stage('Build') { steps { sh "make ${config.target ?: 'build'}" } }
      stage('Test')  { steps { sh "make test" } }
      stage('Package') {
        when { expression { config.package } }
        steps { sh "make package" }
      }
    }
  }
}
