#!/bin/sh
set -e

#docker run --rm -d --name some-logstash --link some-rabbit --link myelastic:localhost mylogstash
#docker run --rm -d -p 1880:1880 --name some-nodered -v /media/pi/ext250/nodered_data:/data mynodered
#docker run -d --rm --name some-elasticsearch -v /media/pi/ext250/elastic_data:/usr/share/elasticsearch/data -p 9200:9200 -p 9300:9300 elasticsearch

docker run -p 5601:5601 --link some-elasticsearch:myelastic-url -e ELASTICSEARCH_URL=http://myelastic-url:9200 --name some-kibana -d kibana
