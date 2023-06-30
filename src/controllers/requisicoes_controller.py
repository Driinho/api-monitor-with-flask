from src.models.models import db, Endereco, Incidente

import requests as http
import platform, subprocess

class RequisicoesController:
    def get_all():
        lista = Endereco.query.filter_by(status=True).all()

        resposta = []

        for endereco in lista:
            if not endereco.ping:
                try:
                    response = http.get(endereco.endereco)
                    
                    dicionario = {
                        "nome_do_sistema": endereco.nome_do_sistema,
                        "endereco": endereco.endereco,
                        "tempo_de_resposta": f"{response.elapsed.total_seconds()} seg",
                        "status_code": response.status_code
                    }
                except:
                    dicionario = {
                        "nome_do_sistema": endereco.nome_do_sistema,
                        "endereco": endereco.endereco,
                        "status_code": 'ERRO'
                    }
            else:
                system = platform.system()

                if system == "Windows":
                    # Ping para Windows
                    response = subprocess.call(['ping', '-n', '3', endereco.endereco])
                else:
                    # Ping para Linux
                    response = subprocess.call(['ping', '-c', '3', endereco.endereco])

                if response == 0:
                    dicionario = {
                        "nome_do_sistema": endereco.nome_do_sistema,
                        "endereco": endereco.endereco,
                        "status_code": 'OK'
                    }
                else:
                    dicionario = {
                        "nome_do_sistema": endereco.nome_do_sistema,
                        "endereco": endereco.endereco,
                        "status_code": 'ERRO'
                    }

            if dicionario.get('status_code') == 'ERRO':
                if not Incidente.query.filter(Incidente.endereco.has(id=endereco.id), Incidente.data_hora_retorno.is_(None)).first():
                    incidente = Incidente(
                        endereco=endereco,
                        data_hora_queda=db.func.now()
                    )

                    db.session.add(incidente)
                    db.session.commit()
            else:
                if Incidente.query.filter(Incidente.endereco.has(id=endereco.id), Incidente.data_hora_retorno.is_(None)).first():
                    
                    db.session.query(Incidente).filter(Incidente.endereco.has(id=endereco.id), Incidente.data_hora_retorno.is_(None)).update({"data_hora_retorno": db.func.now()})
                    
                    db.session.commit()
                
            resposta.append(dicionario)
        
        return resposta

    def get_one(id):
        try:
            endereco = Endereco.query.filter_by(id=id, status=True).first()

            response = http.get(endereco.endereco)
            
            dicionario = {
                "nome_do_sistema": endereco.nome_do_sistema,
                "endereco": endereco.endereco,
                "tempo_de_resposta": f"{response.elapsed.total_seconds()} seg",
                "status_code": response.status_code
            }
        except:
            dicionario = {
                "nome_do_sistema": endereco.nome_do_sistema,
                "endereco": endereco.endereco,
                "status_code": 'ERRO'
            }
        
        return dicionario