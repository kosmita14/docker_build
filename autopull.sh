#!/bin/bash
#set -e

grep -rnw './' -e "image:" --include="docker-compose.yml" |column -t 
grep -rnw './' -e "image:" --include="docker-compose.yml" |column -t |awk '{ print $3; }' |xargs -n1 docker pull 


grep -rnw './' -e "FROM" --include="Dockerfile" |column -t
grep -rnw './' -e "FROM" --include="Dockerfile" |column -t|awk '{ print $2; }'|xargs -n1 docker pull
