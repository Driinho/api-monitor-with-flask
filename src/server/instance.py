from flask import Flask
from flask_restx import Api
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from src.models.models import db, Endereco, Incidente

class Server():
    def __init__(self):
        self.app = Flask(__name__)
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.sqlite'
        db.init_app(self.app)
        migrate = Migrate(self.app, db, render_as_batch=True)
        self.api = Api(self.app,
            title='Api Monitor',
            version='1.0',
            description='Está API tem como objetivo monitorar os serviços da empresa',
            doc='/docs'
        )

    def run(self):
        if __name__ == '__main__':
            self.app.run(debug=True)

server = Server()