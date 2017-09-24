#!/bin/bash
#set -e

#images="$(docker images --no-trunc --digests --format "{{.Repository}}")"
#docker inspect --format='{{range .Mounts}}{{.Source}}{{end}}' some-rabbit
containers="$(docker container ls --format "{{.Names}}")"

if [ "$containers" != "" ] 
then
    for container in $containers
    do
        if [[ ! $container =~ "none" ]]
        then
            #docker pull $image |grep -C 99999 --color 'Status'
            echo "Container: " $container |grep -C 99999 --color 'Container'
            mounts="$(docker inspect --format="{{range .Mounts}}{{.Source}}{{end}}" $container)"
            echo "           " $mounts
        fi
    done
else
    echo "Containers list is empty  !"
fi

