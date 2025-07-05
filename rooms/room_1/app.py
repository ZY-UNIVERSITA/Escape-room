from flask import Flask, request, jsonify, abort
import logging

app = Flask(__name__)
app.logger.setLevel(logging.INFO)

__equation: str = "x + 4 = 168"
CORRECT_ANSWER: int = 41

SECRET_CODE: int = 1

@app.route("/", methods=["GET"])
def start():
    message = {
        "status": "ok",
        "message": f"Per poter proseguire nella prossima stanza, devi risolvere la seguente equazione che dovrai specchiare e il codice segreto ti sarà rivelato.",
        "puzzle": __equation,
    }

    return jsonify(message)

@app.route("/answer", methods=["POST"])
def answer():
    if not request.json:
        abort(415, description="La richiesta di tipo POST non era un JSON.")

    data = request.get_json()
    if "answer" not in data:
        abort(400, description="Il campo 'answer' non è presente.")

    try:
        answer: int = int(data.get("answer"))
    except ValueError:
        abort(400, description="Il campo 'answer' non è un numero.")

    app.logger.info(f"Risposta utente: {answer}")

    if answer == CORRECT_ANSWER:
        message = {
            "status": "ok",
            "message": f"La tua risposta è corretta. Hai ricevuto un oggetto, il numero: ${SECRET_CODE}",
            "object": SECRET_CODE,
        }
    else:
        message = {"status": "wrong", "message": "Risposta sbagliata, riprova"}

    return jsonify(message)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
