from flask import current_app, jsonify, request
from . import codigoPostalBP
from src.models.codigopostal import CodigoPostal
from src.schemas.codigopostalschema import CodigoPostalSchema

@codigoPostalBP.route("/codigospostales/", methods=['Get'])
def getAllCodigosPostales():
    codigosPostalesSchema = CodigoPostalSchema(many=True)
    # model
    codigosPostales = CodigoPostal.getAllCPs()
    return codigosPostalesSchema.jsonify(codigosPostales)

@codigoPostalBP.route("/codigopostal/<int:id>", methods=['Get'])
def getCPById(id):
    codigoPostalSchema = CodigoPostalSchema()
    # model
    codigoPostal = CodigoPostal.getCPById(id)
    return codigoPostalSchema.jsonify(codigoPostal)

@codigoPostalBP.route("/codigopostal/", methods=['Post'])
def createCodigoPostal():
    id = request.json['id']
    nuevoCodigoPostal = CodigoPostal(id)
    nuevoCodigoPostal.createCP()
    
    return jsonify({
        'ok' : True,
        'message' : 'Creado con exito'
    })
