from src.models.models import db, Endereco

class EnderecoController:
    
    def get_all():
        return Endereco.query.filter_by(status=True).all()
    
    def get_by_id(id):
        return Endereco.query.filter_by(id=id, status=True).first()
    
    def create_endereco(json):
        endereco = Endereco(
            nome_do_sistema=json.get('nome_do_sistema'), 
            endereco=json.get('endereco'), 
            ping=json.get('ping')
        )

        db.session.add(endereco)
        db.session.commit()

        return endereco
    
    def att_endereco(id, json):
        endereco = {
            "id": id,
            "nome_do_sistema": json.get('nome_do_sistema'), 
            "endereco": json.get('endereco'), 
            "ping": json.get('ping')
        }

        atualizou = db.session.query(Endereco).filter_by(id=id).update(endereco)
        db.session.commit()

        if not atualizou:
            return 0

        return endereco
    
    def del_endereco(id):
        deletou = db.session.query(Endereco).filter_by(id=id).update({"status": False})
        db.session.commit()

        if not deletou:
            return 0
        
        return Endereco.query.filter_by(id=id).first()
