#!/bin/sh
set -e

#docker run -d -p 9600:9600 --name some-logstash --link some-rabbit --link some-elasticsearch:localhost mylogstash
#docker run -d --net=host -p 9600:9600 --name some-logstash mylogstash
docker-compose up -d --scale logstash=2 --scale logstash_alpine=2 --remove-orphans

