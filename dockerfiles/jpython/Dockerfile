FROM python:3.7-slim

ENV WEB_ROOT_PATH /opt/app
ENV FLASK_LOG_DIR_PATH /var/log/flask/

RUN useradd juser

RUN mkdir -p $WEB_ROOT_PATH
RUN mkdir -p $FLASK_LOG_DIR_PATH
RUN chown juser:juser $WEB_ROOT_PATH
RUN chown juser:juser $FLASK_LOG_DIR_PATH
RUN chmod 755 $WEB_ROOT_PATH
RUN chmod 755 $FLASK_LOG_DIR_PATH

RUN apt-get update
RUN apt-get install -y python3-pip curl vim
RUN pip3 install Flask

COPY app.py ${WEB_ROOT_PATH}/app.py
RUN chown juser:juser ${WEB_ROOT_PATH}/app.py
RUN chmod 755 ${WEB_ROOT_PATH}/app.py

USER juser
