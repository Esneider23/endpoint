from flask import Flask, render_template, jsonify, request

server = Flask(__name__)


@server.get('/')
def index():
    return "Word"


if __name__ == '__main__':
    server.run(debug=True)