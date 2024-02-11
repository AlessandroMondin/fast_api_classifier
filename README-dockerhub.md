# Pull Image into EC2 Instance

### Push local Image to DockerHub

        docker login --username yourUsername
        docker tag myfastapiapp:latest alessandromondin/fast_api_app:tag
        docker push yourUsername/fast_api_app:tag

### Pull image from DockerHub to Amazon Linux ec2 Instance (t2.medium)

        sudo yum update -y
        sudo yum install docker -y
        sudo systemctl start docker
        sudo docker login --username yourUsername
        sudo docker pull yourUsername/yourRepository:yourTag
        docker run -d yourUsername/yourRepository:yourTag
