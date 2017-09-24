#!/bin/sh
set -e

#docker run --rm -d --name some-logstash --link some-rabbit --link myelastic:localhost mylogstash
#docker run -d --rm --name some-elasticsearch -v /media/pi/ext250/elastic_data:/usr/share/elasticsearch/data -p 9200:9200 -p 9300:9300 elasticsearch

docker run -d --name some-netdata --net=host --cap-add SYS_PTRACE -v /proc:/host/proc:ro -v /sys:/host/sys:ro -v /var/run/docker.sock:/var/run/docker.sock -p 19999:19999 --privileged titpetric/netdata
