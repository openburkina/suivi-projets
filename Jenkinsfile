pipeline{  
  agent{
    dockerfile{
      filename 'Dockerfile.build'
    }
  }
  stages{
    stage('deploy to dev'){
      agent any
        when{
          branch 'dev'
        }
      steps{
        echo 'Deploy app with docker compose'
        sh 'docker-compose -f local.yml build'
        sh 'docker-compose -f local.yml up -d'
    }
  }
}