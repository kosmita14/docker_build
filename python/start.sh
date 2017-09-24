#!/bin/sh
set -e

docker run -d --net=host -p 15672:15672 -p 5672:5672 --name some-rabbit --hostname localhost myrabbitmq
