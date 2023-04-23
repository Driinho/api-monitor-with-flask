from flask_restx import fields
from src.server.instance import server

endereco = server.api.model('Endereco', {
    'id': fields.Integer(description='ID do Endereço'),
    'nome_do_sistema': fields.String(required=True, description='Nome do Sistema'),
    'endereco': fields.String(required=True, description='Endereço'),
    'ping': fields.Boolean(required=True, description='Ping')
})

endereco_post = server.api.model('Endereco_post', {
    'nome_do_sistema': fields.String(required=True, description='Nome do Sistema'),
    'endereco': fields.String(required=True, description='Endereço'),
    'ping': fields.Boolean(required=True, description='Ping')
})
