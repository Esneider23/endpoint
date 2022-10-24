from flask import Flask, render_template, jsonify, request
import controller

server = Flask(__name__)


@server.route('/')
def index():
    return "word"


if __name__ == '__main__':
    server.run(debug=True)