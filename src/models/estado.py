from sqlalchemy.exc import IntegrityError
from src import db

class Estado(db.Model):
    __tablename__='estado'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50))
    estado = db.relationship('Municipio', lazy=True, cascade='all, delete-orphan')
    
    def __init__(self, id, nombre):
        self.id = id
        self.nombre = nombre
    
    def createEstado(self):
        db.session.add(self)
        db.session.commit()
    
    @staticmethod
    def getAllEstados():
        return Estado.query.all()
    
    @staticmethod
    def getEstadoById(id):
        return Estado.query.get(id)
    
    @staticmethod
    def getEstadoByName(nombre):
        return Estado.query.filter(Estado.nombre.like('%{}%'.format(nombre))).all()