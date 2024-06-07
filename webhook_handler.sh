#!/bin/bash

COMPOSE_FILE_PATH=/home/ubuntu/dev/SRE_final/

# Change to the directory
cd $COMPOSE_FILE_PATH

# Log output
GIT_LOG=/home/ubuntu/dev/SRE_final/git_pull.log
docker-compose -f $COMPOSE_FILE_PATH pull >> $GIT_LOG 2>&1
git pull >> $GIT_LOG 2>&1

# Pull the latest images
docker-compose pull

# Restart the services
docker-compose up -d --remove-orphans

# Optional: Remove old images
