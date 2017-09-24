#!/bin/sh
set -e

docker run -d --name some-elasticsearch -v /media/pi/ext250/elastic_data:/usr/share/elasticsearch/data -p 9200:9200 -p 9300:9300 elasticsearch
