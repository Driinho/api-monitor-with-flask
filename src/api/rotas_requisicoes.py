from flask_restx import Resource

from src.models.Respostas import resposta
from src.server.instance import server
from src.controllers.requisicoes_controller import RequisicoesController

app, api = server.app, server.api

@api.route('/api/status')
class RotasRequests(Resource):
    @api.marshal_with(resposta)
    def get(self):
        return RequisicoesController.get_all(), 200