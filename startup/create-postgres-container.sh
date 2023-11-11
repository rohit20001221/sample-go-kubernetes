#!/bin/bash

# create docker volume
docker volume create postgres-som

# start the docker container and attach it with the volume
docker run \
    --name postgres-som \
    -p 5432:5432 \
    -e POSTGRES_USER=som \
    -e POSTGRES_DB=som \
    -e POSTGRES_PASSWORD=som!@# \
    -v postgres-som:/var/lib/postgresql/data \
    -d \
    postgres:alpine