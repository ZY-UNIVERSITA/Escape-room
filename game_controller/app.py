from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

PUZZLE_ROOM_1_URL = "http://puzzle_room_1:5001"

@app.rout("/home", methods=["GET"])
def start():
    print("Ricevuta azione: start")

    response = requests.get(f"{PUZZLE_ROOM_1_URL}/home")
    return jsonify({"response_from_puzzle": response.json()})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
