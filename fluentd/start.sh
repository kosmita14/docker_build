#!/bin/sh
set -e
#--log-opt fluentd-async-connect=true
#--log-driver=fluentd --log-opt tag=docker.fluentd

#docker run --rm -d --name some-fluentd -p 24224:24224 -p 24224:24224/udp --link some-elasticsearch:localhost --link some-rabbit -v /media/pi/ext250/fluentd_data:/fluentd/log --log-driver=fluentd --log-opt tag=docker.fluentd --log-opt fluentd-async-connect=true myfluentd
#docker run -d --name some-fluentd -p 24224:24224 -p 24224:24224/udp --link some-rabbit -v /media/pi/ext250/fluentd_data:/fluentd/log myfluentd

docker run -d --net=host --name some-fluentd -p 24224:24224 -p 24224:24224/udp -v /media/pi/ext250/fluentd_data:/fluentd/log myfluentd

