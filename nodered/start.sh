#!/bin/sh
set -e

#docker run --rm -d -p 1880:1880 --name some-nodered -v /media/pi/ext250/nodered_data:/data mynodered
docker run -d -p 1880:1880 --name some-nodered -v /media/pi/ext250/nodered_data:/data mynodered
