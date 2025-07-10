from flask import Flask, jsonify
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="http://game_controller:5000")

@socketio.on('connect')
def handle_connect():
    print('Client connected to Game Engine')

@app.route('/')
def start():
    return jsonify({"status": "Connected to Game Engine"})

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5001)