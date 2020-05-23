FROM ubuntu:latest

ENV WEB_ROOT_PATH /opt/app

RUN mkdir -p $WEB_ROOT_PATH
RUN apt-get update
RUN apt-get install -y python3-pip
RUN pip3 install Flask

COPY app.py ${WEB_ROOT_PATH}/app.py

RUN chmod 755 ${WEB_ROOT_PATH}/app.py
