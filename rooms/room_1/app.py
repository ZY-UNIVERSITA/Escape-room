from flask import Flask, request, jsonify

app = Flask(__name__)

__equation: str = "x + 4 = 168"
__answer: int = 4114

__secret_code: int = 1

@app.route("/", methods=["GET"])
def start():
    message = {
        "status": "ok",
        "message": f"Per poter proseguire nella prossima stanza, devi risolvere la seguente equazione che dovrai specchiare e il codice segreto ti sarà rivelato.",
        "puzzle": __equation
    }

    return jsonify(message)


@app.route("/answer", methods=["POST"])
def answer():
    answer: int = request.json.get("answer")

    message = {}

    if answer != __answer:
        message["status"] = "ok"
        message["message"] = f"La tua risposta è corretta. Hai ricevuto un oggetto, il numero: ${__secret_code}",
        message["object"] =  __secret_code
    else:
        message["status"] = "wrong"
        message["message"] = f"La tua risposta è sbagliata. Riprova."

    return jsonify(message)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
