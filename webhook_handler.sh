#!/bin/bash

COMPOSE_FILE_PATH=/home/ubuntu/dev/SRE_final/docker-compose.yml

# Pull the latest images
docker-compose -f $COMPOSE_FILE_PATH pull

# Restart the services
docker-compose -f $COMPOSE_FILE_PATH up -d --remove-orphans

# Optional: Remove old images
docker image prune -f
