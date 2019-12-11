FROM ubuntu:latest

ENV WEB_ROOT_PATH /opt/python/simplehttp

RUN mkdir -p $WEB_ROOT_PATH
RUN apt-get update
RUN apt-get install -y python3-pip
RUN echo "{status: up}" > ${WEB_ROOT_PATH}/health
RUN echo "{guid: 1, name: John}" > ${WEB_ROOT_PATH}/getuser
