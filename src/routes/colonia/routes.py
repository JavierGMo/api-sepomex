from flask import current_app, jsonify, request
from . import coloniaBP
from src.models.colonia import Colonia
from src.schemas.coloniaschema import ColoniaSchema

@coloniaBP.route("/colonias/", methods=['Get'])
def getAllColonias():
    coloniasSchema = ColoniaSchema(many=True)
    colonias = Colonia.getAllColonias()
    return coloniasSchema.jsonify(colonias)

@coloniaBP.route("/colonia/<int:id>", methods=['Get'])
def getColoniaById(id):
    coloniaSchema = ColoniaSchema()
    colonia = Colonia.getColoniaById(id)
    return coloniaSchema.jsonify(colonia)

@coloniaBP.route("/colonianombre/<string:nombre>", methods=['Get'])
def getColoniaByName(nombre):
    coloniasSchema = ColoniaSchema(many=True)
    colonias = Colonia.getColoniaByName(nombre)
    return coloniasSchema.jsonify(colonias)

@coloniaBP.route("/colonia/", methods=['Post'])
def createColonia():
    
    id = request.json['id']
    nombre = request.json['nombre']
    idmunicipio = request.json['idmunicipio']
    idcp = request.json['idcp']
    
    nuevaColonia = Colonia(id, nombre, idmunicipio, idcp)
    nuevaColonia.createMunicipio()

    return jsonify({
        'ok' : True,
        'message' : 'Colonia creada'
    })

@coloniaBP.route("/coloniacp/<int:idcp>")
def getColoniaByCP(idcp):
    coloniasSchema = ColoniaSchema(many=True)
    colonia = Colonia.getColoniaByCP(idcp)
    return coloniasSchema.jsonify(colonia)