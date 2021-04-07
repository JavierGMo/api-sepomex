from sqlalchemy.exc import IntegrityError
from src import db

class Municipio(db.Model):
    __table_args__={'extend_existing': True}
    __tablename__='municipio'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50))
    idestado = db.Column(db.Integer, db.ForeignKey('estado.id'))
    colonia = db.relationship('Colonia', lazy=True, cascade='all, delete-orphan')

    def __init__(self, id, nombre, idestado):
        self.id = id
        self.nombre = nombre
        self.idestado = idestado
    
    def createMunicipio(self):
        db.session.add(self)
        db.session.commit()
    
    @staticmethod
    def getAllMunicipio():
        return Municipio.query.all()
    
    @staticmethod
    def getEstadoById(id):
        return Municipio.query.get(id)
