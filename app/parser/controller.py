from flask import Blueprint, request, jsonify
from flask_cors import cross_origin, CORS
from app.parser.service import getParsingResult

parser_bp = Blueprint("parser_bp", __name__)
@parser_bp.route('/parse', methods = ['POST'])
def index():
    req_data = request.json
    res, tree = getParsingResult(req_data["sentence"])
    if res:
        return jsonify(result=res, tree=tree)
    return jsonify(result=res)