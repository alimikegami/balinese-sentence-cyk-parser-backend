from flask import Flask, jsonify, request
import cyk_parser
import argparse
import grammar_converter
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)

@app.route('/parse', methods = ['POST', 'OPTIONS'])
@cross_origin(origin='*')
def index():
    req_data = request.get_json()
    response = jsonify(hello=req_data)
    return response

if __name__ == "__main__":
    argparser = argparse.ArgumentParser()
    argparser.add_argument("grammar",
                           help="File containing the grammar or string directly representing the grammar.")
    argparser.add_argument("sentence",
                           help="File containing the sentence or string directly representing the sentence.")
    args = argparser.parse_args()
    CYK = cyk_parser.Parser(args.grammar, args.sentence)
    CYK.parse()
    CYK.print_tree()
    app.run(debug=True)