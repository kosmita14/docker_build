#!/bin/sh
set -e

#docker run -d --rm --name some-elasticsearch -v /media/pi/ext250/elastic_data:/usr/share/elasticsearch/data -p 9200:9200 -p 9300:9300 --log-driver=fluentd --log-opt tag=docker.elasticsearch elasticsearch
docker run -d --name some-portainer -p 9000:9000 -v /var/run/docker.sock:/var/run/docker.sock portainer/portainer

