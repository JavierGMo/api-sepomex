from flask import Blueprint
estadoBP = Blueprint('estado', __name__)
from . import routes