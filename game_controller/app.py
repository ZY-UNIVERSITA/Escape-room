from flask import Flask, request, jsonify
import requests
import logging
import os

app = Flask(__name__)

app.logger.setLevel(logging.INFO)

PUZZLE_ROOM_URL = {
    "1": "http://puzzle_room_1:5001",
    "2": "http://puzzle_room_2:5002"
}

current_room: int = 1
game_state = {
    "solved_rooms": [],
    "inventory": {
    }
}

@app.route("/", methods=["GET"])
def home():
    return app.send_static_file("index.html")

@app.route("/start", methods=["GET"])
def start():
    global current_room

    response = requests.get(f"{PUZZLE_ROOM_URL[str(current_room)]}/")
    data = response.json()

    return jsonify(data)


@app.route("/answer", methods=["POST"])
def answer():
    global current_room

    action = request.json.get("answer")
    
    app.logger.info(f"Risposta utente: {action}")

    response = requests.post(f"{PUZZLE_ROOM_URL[str(current_room)]}/answer", json={"answer": action})

    try:
        data = response.json()
    except ValueError:
        data = {}

    if (data.get("status")) == "ok":
        if data.get("object"):
            game_state["inventory"][current_room] = data.get("object")

        game_state["solved_rooms"].append(current_room)

        current_room += 1


    return jsonify(data)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
