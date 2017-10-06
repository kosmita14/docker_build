#!/bin/sh
#set -e

docker-compose build

#all_images="$(docker images logstash --format "{{.ID}}")"

#if [ "$all_images" != "" ] 
#then
#    docker rmi "$all_images"
#else
#    echo "All good - no images found !"
#fi



#all_images="$(docker images mylogstash --format "{{.ID}}")"

#if [ "$all_images" != "" ] 
#then
#    docker rmi "$all_images"
#else
#    echo "All good - no images found !"
#fi


#docker build -t mylogstash ./
