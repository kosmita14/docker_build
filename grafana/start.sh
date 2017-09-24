#!/bin/sh
set -e

#docker run -d --name some-portainer -p 9000:9000 -v /var/run/docker.sock:/var/run/docker.sock portainer/portainer
docker run -d --name=grafana -p 3000:3000 grafana/grafana
