from src.models.models import db, Endereco, Incidente

class IncidentesController:
    def get_all():
        return db.session.query(Incidente).join(Endereco).all()
