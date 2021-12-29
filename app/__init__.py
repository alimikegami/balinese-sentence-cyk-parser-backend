from flask import Flask
from flask_cors import CORS
from app.parser.controller import parser_bp

def balinese_sentence_app(debug=False):
    app = Flask(__name__)
    CORS(app)    
    app.register_blueprint(parser_bp)
    return app