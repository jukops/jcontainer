#!/usr/bin/python3

from flask import Flask, request
from datetime import datetime

app = Flask(__name__)

now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

@app.route("/")
def root_app():
  print(request.base_url, "is called at", dt_string)
  return "{\"msg\": \"root is called\"}"

@app.route("/auth")
def auth_app():
  print(request.base_url, "is called at", dt_string)
  return "{\"msg\": \"auth is called\"}"

@app.route("/user")
def user_app():
  print(request.base_url, "is called at", dt_string)
  return "{\"msg\": \"username is jh\"}"

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8080)
