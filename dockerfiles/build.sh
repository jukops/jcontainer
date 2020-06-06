#!/bin/bash

REPO="localhost:5000"
APP=""
TAG=""

if [[ $1 = "" ]]; then
  echo "Please enter app name"
  exit 1
else
 APP=$1
fi

if [[ -z $2 ]]; then
  TAG="latest"
else
  TAG=$2
fi

docker build -t ${REPO}/${APP}:${TAG} ./${APP}
docker push ${REPO}/${APP}:${TAG}
