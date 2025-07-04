from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

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
def start():
    response = requests.get(f"{PUZZLE_ROOM_URL[str(current_room)]}/")

    return jsonify(response)

@app.route("/answer", methods=["POST"])
def answer():
    action = request.json.get("answer")

    response = requests.post(f"{PUZZLE_ROOM_URL[str(current_room)]/answer}", json={"answer": action})

    if (response.json.get("status")) == "ok":
        if response.json.get("object"):
            game_state["inventory"][current_room] = response.json.get("object")

        game_state["solved_rooms"].append(current_room)

        current_room += 1

    return jsonify(response)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
