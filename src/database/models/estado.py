from flask import Flask
from flask_marshmallow import Marshmallow
"""
from app import db

class Estado(db.Model):
    
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50))
    def __init__(self, id, nombre):
        self.id = id
        self.nombre = nombre
    def createEstado(self):
        db.session.add(self)
        db.session.commit()
    def getAllEstados(self):
        return Estado.query.all()
    def getEstadoById(self, id):
        return Estado.query.get(id)
"""