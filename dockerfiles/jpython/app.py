#!/usr/bin/python3

from flask import Flask, request
from datetime import datetime
import logging

log_file_path = '/var/log/flask/app.log'
log_format = '[%(levelname)s] [%(asctime)s]: %(message)s'
logging.basicConfig(filename = log_file_path,
                    level = logging.INFO,
                    format = log_format
                    )

app = Flask(__name__)

@app.route("/", methods=['GET'])
def root_app():
  try:
    user = request.args.get('user')

    if user is None:
      app.logger.info("no user in request")
    else:
      app.logger.info("%s called %s", user, request.base_url)
  except Exception as ex:
    app.logger.info("exception is catched")
    app.logger.info("%s", ex)

  return "{\"msg\": \"root is called\"}"

@app.route("/auth")
def auth_app():
  try:
    user = request.args.get('user')
  
    if user is None:
      app.logger.info("no user in request")
    else:
      app.logger.info("%s called %s", user, request.base_url)
  except Exception as ex:
    app.logger.info("exception is catched")
    app.logger.info("%s", ex)

  return "{\"msg\": \"auth is called\"}"

@app.route("/user")
def user_app():
  try:
    user = request.args.get('user')
  
    if user is None:
      app.logger.info("no user in request")
    else:
      app.logger.info("%s called %s", user, request.base_url)
  except Exception as ex:
    app.logger.info("exception is catched")
    app.logger.info("%s", ex)
    
  return "{\"msg\": \"username is jh\"}"

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8080)
