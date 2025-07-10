from flask import Flask, jsonify
from flask_socketio import SocketIO
import logging

app = Flask(__name__)
app.logger.setLevel(logging.INFO)

socketio = SocketIO(app, cors_allowed_origins="http://127.0.0.1:5000")

@socketio.on('connect')
def handle_connect():
    app.logger.info('Client connected to Game Engine')

@app.route('/')
def start():
    return jsonify({"status": "Connected to Game Engine"})

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5001)