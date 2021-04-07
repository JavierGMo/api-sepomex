from sqlalchemy.exc import IntegrityError
from src import db

class CodigoPostal(db.Model):
    __tablename__='codigopostal'
    id = db.Column(db.Integer, primary_key=True)
    colonia = db.relationship('Colonia', lazy=True, cascade='all, delete-orphan')
    def __init__(self, id, nombre):
        self.id = id
        self.nombre = nombre
    
    def createCP(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def getAllCPs():
        return CodigoPostal.query.all()
    
    @staticmethod
    def getCPById(id):
        return CodigoPostal.query.get(id)