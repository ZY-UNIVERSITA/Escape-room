from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/home", methods=["GET"])
def start():
    return jsonify({"status": "ok", "message": f"Inizio puzzle"})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5001)
