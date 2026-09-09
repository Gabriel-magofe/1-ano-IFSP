from flask import Flask, render_template, jsonify
import subprocess
import os

app = Flask(__name__)

CAMINHO_EXE = os.path.abspath("GALINHADANGOLINATOR.exe")

@app.route("/")
def inicio():
    return render_template("index.html")

@app.route("/executar", methods=["POST"])
def executar():
    try:
        subprocess.Popen([CAMINHO_EXE])
        return jsonify({
            "sucesso": True,
            "mensagem": "Programa iniciado."
        })
    except Exception as erro:
        return jsonify({
            "sucesso": False,
            "mensagem": str(erro)
        }), 500

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=False)
