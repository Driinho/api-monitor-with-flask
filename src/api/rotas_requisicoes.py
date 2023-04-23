from flask_restx import Resource
from .db import Enderecos

from src.models.Respostas import resposta
from src.server.instance import server

import requests as http
import platform, subprocess

app, api = server.app, server.api

@api.route('/api/status')
class RotasRequests(Resource):
    @api.marshal_with(resposta)
    def get(self):

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

        return lista, 200