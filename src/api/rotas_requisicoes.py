from flask_restx import Resource

from src.models.Respostas import resposta
from src.server.instance import server

from src.models.models import db, Endereco

import requests as http
import platform, subprocess

app, api = server.app, server.api

@api.route('/api/status')
class RotasRequests(Resource):
    @api.marshal_with(resposta)
    def get(self):
        lista = db.session.query(Endereco).all()

        resposta = []

        for endereco in lista:
            if not endereco.ping:
                try:
                    response = http.get(endereco.endereco)
                    
                    dicionario = {
                        "nome_do_sistema": endereco.nome_do_sistema,
                        "endereco": endereco.endereco,
                        "tempo_de_resposta": f"{response.elapsed.total_seconds()} segundos",
                        "status_code": response.status_code
                    }
                except:
                    dicionario = {
                        "nome_do_sistema": endereco.nome_do_sistema,
                        "endereco": endereco.endereco,
                        "status_code": 'ERRO'
                    }
            else:
                system = platform.system()

                if system == "Windows":
                    # Ping para Windows
                    response = subprocess.call(['ping', '-n', '3', endereco.endereco])
                else:
                    # Ping para Linux
                    response = subprocess.call(['ping', '-c', '3', endereco.endereco])

                if response == 0:
                    dicionario = {
                        "nome_do_sistema": endereco.nome_do_sistema,
                        "endereco": endereco.endereco,
                        "status_code": 'OK'
                    }
                else:
                    dicionario = {
                        "nome_do_sistema": endereco.nome_do_sistema,
                        "endereco": endereco.endereco,
                        "status_code": 'ERRO'
                    }
                
            resposta.append(dicionario)

        return resposta, 200