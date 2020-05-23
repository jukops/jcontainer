#!/usr/bin/python3

from flask import Flask

app = Flask(__name__)

@app.route("/")
def root_app():
  return "{\"msg\": \"root is called\"}"

@app.route("/auth")
def auth_app():
  return "{\"msg\": \"auth is called\"}"

@app.route("/user")
def user_app():
  return "{\"msg\": \"username is jh\"}"

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8080)
