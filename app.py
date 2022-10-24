from flask import Flask, render_template, jsonify, request
import requests
import controller

server = Flask(__name__)


@server.route('/')
def index():
    return jsonify({"Message": "Welcome to apy"})


if __name__ == '__main__':
    server.run(debug=True)