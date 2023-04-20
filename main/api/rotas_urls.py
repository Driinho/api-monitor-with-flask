from flask import Blueprint

bp_urls = Blueprint('bp_urls', __name__)

@bp_urls.route('/urls')
def api_index():
    return 'Estou em Rotas de Urls !!'