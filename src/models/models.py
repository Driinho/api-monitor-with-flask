from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Endereco(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome_do_sistema = db.Column(db.String(80), nullable=False)
    endereco = db.Column(db.String(120), nullable=False)
    ping = db.Column(db.Boolean, nullable=False)
    status = db.Column(db.String(120), default=True)

class Incidente(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    endereco = db.Column(db.String(120), nullable=False)
    data_hora_queda = db.Column(db.DateTime, nullable=False)
    data_hora_retorno = db.Column(db.DateTime, nullable=False)