from flask import Flask, jsonify
import requests
import json

app = Flask(__name__)


@app.route("/funcionarios/registros", methods=['GET'])
def get_registros():
    api_url = "https://jsonplaceholder.typicode.com/todos/1"
    response = requests.get(api_url)
    return jsonify() 


@app.route("/funcionarios/cadastro", methods=['POST'])
def cadastrar():
    api_url = "https://jsonplaceholder.typicode.com/todos"
    envio = {'id': 1, 'cargo': 2, 'cargo': 3}
    response = requests.post(api_url, json=envio)

    return response.json()


@app.route("/funcionarios/deletar", methods=['DELETE'])
def excluir_registro():
    api_url = "https://jsonplaceholder.typicode.com/todos/1"
    response = requests.delete(api_url)

    return response.json()


if __name__ == '__main__':
    app.run()
