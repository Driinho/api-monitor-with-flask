from flask_restx import fields
from src.server.instance import server
from src.models.Enderecos import endereco

incidente = server.api.model('Incidente', {
    'endereco': fields.Nested(endereco, required=True, description='Endereço do incidente'),
    'data_hora_queda': fields.DateTime(required=True, description='Data e hora da queda'),
    'data_hora_retorno': fields.DateTime(required=True, description='Data e hora do retorno'),
})