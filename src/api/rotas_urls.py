from flask import request
from flask_restx import Resource
from .db import Enderecos

from src.models.Enderecos import endereco
from src.models.Enderecos import endereco_post
from src.server.instance import server

app, api = server.app, server.api

@api.route('/api/enderecos')
class RotasEnderecos(Resource):
    # método GET para listar todos os endereços
    @api.marshal_list_with(endereco)
    def get(self):
        return Enderecos, 200
    
    # método POST para criar um novo endereço
    @api.expect(endereco_post, validate=True)
    @api.marshal_list_with(endereco)
    def post(self):
        post = request.get_json()

        new_endereco = {
            "id": len(Enderecos) + 1,
            "nome_do_sistema": post.get('nome_do_sistema'),
            "endereco": post.get('endereco'),
            "ping": post.get('ping')
        }

        Enderecos.append(new_endereco)

        return new_endereco, 201

    @api.doc(params={'id': 'ID do Endereço'})
    @api.route('/api/enderecos/<int:id>')
    class endereco_by_id(Resource):
        # método GET para listar um endereço específico
        @api.marshal_list_with(endereco)    
        def get(self, id):
            for endereco in Enderecos:
                if endereco.get('id') == id:
                    return endereco
                
        # método PUT para editar um endereço específico
        @api.marshal_list_with(endereco)
        def put(self, id):
            post = request.get_json()

            att_endereco = {
                "id": id,
                "nome_do_sistema": post.get('nome_do_sistema'),
                "endereco": post.get('endereco'),
                "ping": post.get('ping')
            }

            for index, endereco in enumerate(Enderecos):
                if endereco.get('id') == id:
                    Enderecos[index] = att_endereco
                    return Enderecos[index]
        
        # método DELETE para deletar um endereço específico
        @api.marshal_list_with(endereco)
        def delete(self, id):
            for endereco in Enderecos:
                if endereco.get('id') == id:
                    endereco_aux = endereco
                    Enderecos.remove(endereco)
                    return endereco_aux

