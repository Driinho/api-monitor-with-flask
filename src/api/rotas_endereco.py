from flask import request, make_response, jsonify
from flask_restx import Resource
from .db import Enderecos

from src.models.Enderecos import endereco
from src.models.Enderecos import endereco_post
from src.server.instance import server
from src.models.models import db, Endereco
from src.controllers.enderecos_controller import EnderecoController


app, api = server.app, server.api

@api.route('/api/enderecos')
class RotasEnderecos(Resource):
    # método GET para listar todos os endereços
    @api.marshal_list_with(endereco)
    def get(self):
        todos_enderecos = EnderecoController.get_all()
        return todos_enderecos, 200
    
    # método POST para criar um novo endereço
    @api.expect(endereco_post, validate=True)
    @api.marshal_list_with(endereco)
    def post(self):
        post = request.get_json()
        endereco_criado = EnderecoController.create_endereco(post)

        return endereco_criado, 201

    @api.doc(params={'id': 'ID do Endereço'})
    @api.route('/api/enderecos/<int:id>')
    class endereco_by_id(Resource):
        # método GET para listar um endereço específico
        @api.marshal_with(endereco)
        def get(self, id):
            endereco = EnderecoController.get_by_id(id)

            if endereco is None:
                return endereco, 404
            else:
                return endereco, 200
                
        # método PUT para editar um endereço específico
        @api.expect(endereco_post, validate=True)
        @api.marshal_list_with(endereco)
        def put(self, id):
            post = request.get_json()

            att_endereco = EnderecoController.att_endereco(id, post)
            
            if att_endereco == 0:
                return att_endereco, 404

            return att_endereco, 200

        # método DELETE para deletar um endereço específico
        @api.marshal_list_with(endereco)
        def delete(self, id):
            del_endereco = EnderecoController.del_endereco(id)

            if not del_endereco:
                return del_endereco, 404
                
            return del_endereco, 200

