from flask import Blueprint
from .rotas_urls import bp_urls
from .request import bp_requests

api = Blueprint('api', __name__, url_prefix='/api')
api.register_blueprint(bp_urls)
api.register_blueprint(bp_requests)

@api.route('/')
def index():
    return 'Estou na Raiz API !!'
