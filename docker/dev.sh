#!/bin/bash

# BUILD DOCKER IMAGES
#docker build -t qooba/feast:ray_dev -f Dockerfile.ray_dev .

docker run -it --rm --network app_default --name feast -p 8888:8888 -v $(pwd)/dataset:/app/dataset --shm-size=5.09gb -v $(pwd)/../../AIDaskFeast/src/feast:/feast-qooba qooba/feast:ray_dev /bin/bash
