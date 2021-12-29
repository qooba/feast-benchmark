#!/bin/bash

# BUILD DOCKER IMAGES
docker build -t qooba/feast:master_test -f Dockerfile.no_dask_test .
docker build -t qooba/feast:dask_test -f Dockerfile.dask_test .
docker build -t qooba/feast:ray_test -f Dockerfile.ray_test .

# GENERATE DATASET
if [ ! -d "daaset" ]; then
  echo 'GENERATE DATASET'
  mkdir dataset
  docker run -it -v $(pwd)/dataset:/app/dataset qooba/feast:master_test /bin/bash -c 'python3 generate.py'
fi

# TEST
echo 'TEST MASTER'
docker run -it -v $(pwd)/dataset:/app/dataset qooba/feast:master_test /bin/bash -c 'python3 run.py'

echo 'TEST DASK'
docker run -it -v $(pwd)/dataset:/app/dataset qooba/feast:dask_test /bin/bash -c 'python3 run.py'

echo 'TEST DASK ON RAY'
docker run -it -v $(pwd)/dataset:/app/dataset --shm-size=5.09gb qooba/feast:ray_test /bin/bash -c 'python3 run_ray.py'


