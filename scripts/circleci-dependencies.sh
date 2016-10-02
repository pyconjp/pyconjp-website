#!/usr/bin/env bash

set -ex

if [ -e ~/docker/wheel.tar ]; then docker load -i ~/docker/wheel.tar; fi
docker info
docker build -f Dockerfile.wheel -t pyconjp/wheelhouse:2016 .
mkdir -p ~/docker; docker save pyconjp/wheelhouse:2016 > ~/docker/wheel.tar

