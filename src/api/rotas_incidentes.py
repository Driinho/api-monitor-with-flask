from flask_restx import Resource

from src.models.Incidentes import incidente
from src.controllers.incidentes_controller import IncidentesController
from src.server.instance import server

app, api = server.app, server.api

@api.route('/api/v1/incidentes')
class RotasIncidentes(Resource):
    @api.marshal_list_with(incidente)
    def get(self):
        todos_incidentes = IncidentesController.get_all()
        return todos_incidentes, 200
