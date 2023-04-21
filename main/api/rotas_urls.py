from flask import Blueprint, jsonify, request
from .db import Enderecos

bp_urls = Blueprint('bp_urls', __name__)

@bp_urls.route('/urls', methods=['GET'])
def getUrls():
    return jsonify(Enderecos)

@bp_urls.route('/urls/<int:id>', methods=['GET'])
def get_endereco_by_id(id):
    for endereco in Enderecos:
        if endereco.get('id') == id:
            return jsonify(endereco)
        
@bp_urls.route('/urls', methods=['POST'])
def criar_endereco():
    post = request.get_json()

    new_endereco = {
        "id": len(Enderecos) + 1,
        "nome_do_sistema": post.get('nome_do_sistema'),
        "endereco": post.get('endereco'),
        "ping": post.get('ping')
    }

    Enderecos.append(new_endereco)

    return jsonify(new_endereco)

@bp_urls.route('/urls/<int:id>', methods=['PUT'])
def editar_endereco(id):
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
            return jsonify(Enderecos[index])

@bp_urls.route('/urls/<int:id>', methods=['DELETE'])
def deletar_endereco(id):
    for endereco in Enderecos:
        if endereco.get('id') == id:
            Enderecos.remove(endereco)
            return jsonify(endereco)

