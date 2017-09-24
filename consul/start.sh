#!/bin/sh
set -e

docker run -it \
   --net=host \
   -e CONSUL_LOCAL_CONFIG='{
    "datacenter":"us_west",
    "server":true,
    "enable_debug":true
    }' \
   consul agent -server -ui -bootstrap-expect=3


