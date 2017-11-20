#!/bin/sh
set -e
LOGGING_DRIVER=fluentd
export LOGGING_DRIVER
docker-compose up -d 
