#!/bin/bash
docker buildx use go-kubernetes

docker buildx build \
    --platform linux/amd64,linux/arm64,linux/arm/v7,linux/arm/v8 \
    -t rohit20001221/sample-kubernetes-go \
    --push \
    .