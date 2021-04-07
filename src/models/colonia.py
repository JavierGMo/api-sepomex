from sqlalchemy.exc import IntegrityError
from src import db


class Colonia(db.Model):
    __table_args__={'extend_existing': True}
    __tablename__='colonia'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50))
    idmunicipio = db.Column(db.Integer, db.ForeignKey('municipio.id'))
    idcp = db.Column(db.Integer, db.ForeignKey('codigopostal.id'))

    def __init__(self, id, nombre, idmunicipio, idcp):
        self.id = id
        self.nombre = nombre
        self.idmunicipio = idmunicipio
        self.idcp = idcp
    

    def createMunicipio(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def getAllColonias():
        return Colonia.query.all()
    
    @staticmethod
    def getColoniaById(id):
        return Colonia.query.get(id)