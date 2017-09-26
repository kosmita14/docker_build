#!/bin/sh
set -e


running_containers="$(docker ps --filter "name=composetest" --format "{{.ID}}")"

if [ "$running_containers" != "" ] 
then
    for container in $running_containers
    do
        docker stop "$container"
    done
else
    echo "All good - no running containers !"
fi



all_containers="$(docker ps -a --filter "name=composetest" --format "{{.ID}}")"

if [ "$all_containers" != "" ] 
then
    for container in $all_containers
    do
        docker rm "$container"
    done
else
    echo "All good - no containers !"
fi





