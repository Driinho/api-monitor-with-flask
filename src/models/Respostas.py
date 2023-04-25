from flask_restx import fields
from src.server.instance import server

resposta = server.api.model('Resposta', {
    'nome_do_sistema': fields.String(required=True, description='Nome do Sistema'),
    'endereco': fields.String(required=True, description='Endereço'),
    'tempo_de_resposta': fields.String(required=True, description='Tempo de Resposta'),
    'status_code': fields.String(required=True, description='Status Code')
})