from flask import request, make_response, jsonify
from flask_restx import Resource
from .db import Enderecos

from src.models.Enderecos import endereco
from src.models.Enderecos import endereco_post
from src.server.instance import server
from src.models.models import db, Endereco

app, api = server.app, server.api

@api.route('/api/enderecos')
class RotasEnderecos(Resource):
    # método GET para listar todos os endereços
    @api.marshal_list_with(endereco)
    def get(self):
        todos_enderecos = Endereco.query.all()
        return todos_enderecos, 200
    
    # método POST para criar um novo endereço
    @api.expect(endereco_post, validate=True)
    @api.marshal_list_with(endereco)
    def post(self):
        post = request.get_json()

        new_endereco = Endereco(
            nome_do_sistema=post.get('nome_do_sistema'), 
            endereco=post.get('endereco'), 
            ping=post.get('ping')
        )

        db.session.add(new_endereco)
        db.session.commit()

        return new_endereco, 201

    @api.doc(params={'id': 'ID do Endereço'})
    @api.route('/api/enderecos/<int:id>')
    class endereco_by_id(Resource):
        # método GET para listar um endereço específico
        @api.marshal_with(endereco)
        def get(self, id):
            endereco_por_id = Endereco.query.filter_by(id=id).first()

            if endereco_por_id is None:
                return endereco_por_id, 404
            else:
                return endereco_por_id, 200
                
        # método PUT para editar um endereço específico
        @api.expect(endereco_post, validate=True)
        @api.marshal_list_with(endereco)
        def put(self, id):
            post = request.get_json()

            att_endereco = {
                "id": id,
                "nome_do_sistema": post.get('nome_do_sistema'),
                "endereco": post.get('endereco'),
                "ping": post.get('ping')
            }
            
            if db.session.query(Endereco).filter_by(id=id).update(att_endereco) == 0:
                db.session.commit()
                return att_endereco, 404
            
            print("======== 68 =========")

            db.session.commit()
            return att_endereco, 200

        # método DELETE para deletar um endereço específico
        @api.marshal_list_with(endereco)
        def delete(self, id):
            del_endereco = Endereco.query.filter_by(id=id).first()

            db.session.query(Endereco).filter_by(id=id).update({"status": False})
            db.session.commit()

            return del_endereco, 204

