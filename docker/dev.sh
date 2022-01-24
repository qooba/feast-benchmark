#!/bin/bash

# BUILD DOCKER IMAGES
#docker build -t qooba/feast:ray_dev -f Dockerfile.ray_dev .

docker run -it -v $(pwd)/../../AIDaskFeast/src/feast:/feast-qooba qooba/feast:ray_dev /bin/bash
