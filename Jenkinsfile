pipeline{ 
    agent any 
  stages{
    stage('deploy to dev'){
      
        when{
          branch 'dev'
        }
      steps{
        echo 'Deploy app with docker compose'
        sh 'docker-compose -f local.yml down'
      }
   }
 }
}