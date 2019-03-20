#!/bin/bash

eval "$(ssh-agent -s)" &&
ssh-add -k ~/.ssh/id_rsa &&
cd /home/ubuntu/nyoba_deploy_aws
git pull

source ~/.profile
echo "$DOCKERHUB_PASS" | sudo docker login --username $DOCKERHUB_USER --password-stdin
sudo docker stop nyoba_deploy_aws
sudo docker rm nyoba_deploy_aws
sudo docker rmi hilmanyr/nyoba_deploy_aws
sudo docker run -d --name nyoba_deploy_aws -p 5002:5002 hilmanyr/nyoba_deploy_aws:latest
