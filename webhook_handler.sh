#!/bin/bash

COMPOSE_FILE_PATH=/home/ubuntu/dev/SRE_final/

cd $COMPOSE_FILE_PATH
git pull
# Pull the latest images
docker-compose pull

# Restart the services
docker-compose up -d --remove-orphans

# Optional: Remove old images

