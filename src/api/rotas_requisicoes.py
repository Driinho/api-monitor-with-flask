from flask_restx import Resource

from src.models.Respostas import resposta
from src.server.instance import server
from src.controllers.requisicoes_controller import RequisicoesController

app, api = server.app, server.api

@api.route('/api/v1/status')
class RotasRequests(Resource):
    @api.marshal_with(resposta)
    def get(self):
        return RequisicoesController.get_all(), 200

    @api.route('/api/v1/status/<int:id>')
    class RotasRequestsUmEndereco(Resource):
        @api.marshal_with(resposta)
        def get(self, id):
            return RequisicoesController.get_one(id), 200