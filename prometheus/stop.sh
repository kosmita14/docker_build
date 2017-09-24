#!/bin/sh
set -e


running_containers="$(docker ps --filter "name=some-prometheus" --format "{{.ID}}")"

if [ "$running_containers" != "" ] 
then
    docker stop "$running_containers"
else
    echo "All good - no running containers !"
fi


all_containers="$(docker ps -a --filter "name=some-prometheus" --format "{{.ID}}")"

if [ "$all_containers" != "" ] 
then
    docker rm "$all_containers"
else
    echo "All good - no containers !"
fi





running_containers="$(docker ps --filter "ancestor=myprometheus" --format "{{.ID}}")"

if [ "$running_containers" != "" ] 
then
    docker stop "$running_containers"
else
    echo "All good - no running containers !"
fi


all_containers="$(docker ps -a --filter "ancestor=myprometheus" --format "{{.ID}}")"

if [ "$all_containers" != "" ] 
then
    docker rm "$all_containers"
else
    echo "All good - no containers !"
fi

