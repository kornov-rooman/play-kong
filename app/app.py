from flask import Flask, jsonify

import socket

app = Flask(__name__)


@app.route('/api/v1/ping')
def ping():
    return jsonify(pong=True)


@app.route('/api/v1/hostname')
def hostname():
    return jsonify(hostname=socket.gethostname())


if __name__ == '__main__':
    app.run()
