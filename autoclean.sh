#!/bin/sh
set -e

docker system prune -a --force

images="$(docker images -f "dangling=true" -q)"

if [ "$images" != "" ] 
then
    docker rmi "$images"
else
    echo "All good !"
fi


docker volume prune --force


