import flask
from flask import jsonify, request
from flask_expects_json import expects_json

from utils import handle_json_data

app = flask.Flask(__name__)

schema = {
    "type": "object",
    "properties": {
            "CustomerID": {"type": "integer"},
        "DwellingCoverage": {"type": "integer", "minimum": 0},
        "HomeAge": {"type": "integer", "minimum": 0},
        "RoofType": {
            "type": "string",
            "pattern": "^(Asphalt Shingles|Tin|Wood)$"},
        "NumberOfUnits": {"type": "integer", "minimum": 1, "maximum": 4},
        "PartnerDiscount": {"type": "string", "pattern": "^(Y|N)$"}
    },
    "required": [
        "CustomerID",
        "DwellingCoverage",
        "HomeAge",
        "RoofType",
        "NumberOfUnits"]
}


@app.route("/", methods=["POST"])
@expects_json(schema)
def rating():
    data = request.get_json()
    value = handle_json_data(data)
    return jsonify(value)


app.run()
