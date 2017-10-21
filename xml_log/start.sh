#!/bin/sh
set -e

docker-compose up --force-recreate --build

#docker-compose up -d --remove-orphans

