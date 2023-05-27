from flask import Flask, jsonify
import json
import requests
import mysql.connector

app = Flask(__name__)

bancoDeDados = mysql.connector.connect(
    host="localhost", user="root", password= '1999', database='Funcionarios')


@app.route("/funcionarios/registros", methods=["GET"])
def listar():
    selectAllSql = f"select * from tb_aluno"
    cursor = bancoDeDados.cursor()
    cursor.execute(selectAllSql)
    resultado = cursor.fetchall()
    if resultado is None:
        api_url = "http://127.0.0.1:5000/funcionarios/registros"
        response = requests.get(api_url)
        retornaApi = response.json()
    else:
        retornaApi = None

    return jsonify(retornaApi)


@app.route("/funcionarios/cadastro", methods=["POST"])
def listar():
    selectAllSql = f"select * from tb_aluno"
    cursor = bancoDeDados.cursor()
    cursor.execute(selectAllSql)
    resultado = cursor.fetchall()
    if resultado is None:
        api_url = "http://127.0.0.1:5000/funcionarios/cadastro"
        response = requests.get(api_url)
        retornaApi = response.json()
    else:
        retornaApi = None

    return jsonify(retornaApi)


@app.route("/funcionarios/deletar", methods=["DELETE"])
def listar():
    selectAllSql = f"select * from tb_aluno"
    cursor = bancoDeDados.cursor()
    cursor.execute(selectAllSql)
    resultado = cursor.fetchall()
    if resultado is None:
        api_url = "http://127.0.0.1:5000/funcionarios/deletar"
        response = requests.get(api_url)
        retornaApi = response.json()
    else:
        retornaApi = None

    return jsonify(retornaApi)


if __name__ == '__main__':
    app.run(port=5001)
