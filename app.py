from flask import Flask, jsonify


app = Flask(__name__)


@app.route("/")
def home():
    return jsonify({"message": "App rodando com Docker"})


@app.route("/soma/<int:a>/<int:b>")
def soma(a, b):
    return jsonify({"resultado": a + b})


@app.route("/subtracao/<int:a>/<int:b>")
def subtracao(a, b):
    return jsonify({"resultado": a - b})


@app.route("/multiplicacao/<int:a>/<int:b>")
def multiplicacao(a, b):
    return jsonify({"resultado": a * b})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
