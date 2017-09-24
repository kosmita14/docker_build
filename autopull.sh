#!/bin/bash
#set -e

#images="$(docker images --no-trunc --digests --format "{{.Repository}}@{{.Digest}}")"
images="$(docker images --no-trunc --digests --format "{{.Repository}}")"

if [ "$images" != "" ] 
then
    for image in $images
    do
        if [[ ! $image =~ "none" ]]
        then
            docker pull $image |grep -C 99999 --color 'Status'
        fi
    done
else
    echo "Images list is empty  !"
fi

#docker pull fluent/fluentd:onbuild
#docker pull logstash
#docker pull nodered/node-red-docker
#docker pull rabbitmq:management

