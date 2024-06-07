#!/bin/bash

COMPOSE_FILE_PATH=/home/ubuntu/dev/SRE_final/docker-compose.yml

docker-compose -f $COMPOSE_FILE_PATH pull

docker-compose -f $COMPOSE_FILE_PATH up -d
