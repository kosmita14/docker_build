#!/bin/sh
set -e

docker run -d -p 9090:9090 --name some-prometheus --net=host myprometheus
