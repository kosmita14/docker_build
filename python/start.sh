#!/bin/sh
set -e

docker run -d --net=host -e TZ=Europe/Warsaw -p 15672:15672 -p 5672:5672 -v "$PWD":/usr/src/app --name some-python --hostname localhost mypython

