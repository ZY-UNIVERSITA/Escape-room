from flask import Flask, request, jsonify

app = Flask(__name__)
SECRET_CODE = "8271"
puzzle_solved = False

@app.route("/", methods=["GET"])
def start():
    return jsonify({"status": "ok"})

@app.route('/answer', methods=['POST'])
def puzzle():
    return


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5003)
