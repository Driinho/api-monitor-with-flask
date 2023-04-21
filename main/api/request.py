from flask import Blueprint, jsonify, request
from .db import Enderecos
import requests as http
import platform, subprocess

bp_requests = Blueprint('bp_requests', __name__)

@bp_requests.route('/status', methods=['GET'])
def get_status():

    lista = []

    for endereco in Enderecos:
        if not endereco.get('ping'):
            try:
                response = http.get(endereco.get('endereco'))

                dicionario = {
                    "nome_do_sistema": endereco.get('nome_do_sistema'),
                    "endereco": endereco.get('endereco'),
                    "status_code": response.status_code
                }
            except:
                dicionario = {
                    "nome_do_sistema": endereco.get('nome_do_sistema'),
                    "endereco": endereco.get('endereco'),
                    "status_code": 'ERRO'
                }
        else:
            system = platform.system()

            if system == "Windows":
                # Ping para Windows
                response = subprocess.call(['ping', '-n', '3', endereco.get('endereco')])
            else:
                # Ping para Linux
                response = subprocess.call(['ping', '-c', '3', endereco.get('endereco')])

            if response == 0:
                dicionario = {
                    "nome_do_sistema": endereco.get('nome_do_sistema'),
                    "endereco": endereco.get('endereco'),
                    "status_code": 'OK'
                }
            else:
                dicionario = {
                    "nome_do_sistema": endereco.get('nome_do_sistema'),
                    "endereco": endereco.get('endereco'),
                    "status_code": 'ERRO'
                }
            
        lista.append(dicionario)

    return jsonify(lista)