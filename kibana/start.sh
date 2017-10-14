#!/bin/sh
set -e

#docker run -p 5601:5601 --link elasticsearch_elasticsearch_1:myelastic-url -e ELASTICSEARCH_URL=http://myelastic-url:9200 --name some-kibana -d kibana
docker run -p 5601:5601 --net host -e ELASTICSEARCH_URL=http://localhost:9200 --name some-kibana -d kibana
