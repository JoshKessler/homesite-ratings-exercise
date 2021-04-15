import flask
from flask import jsonify, request

from utils import handle_json_data

app = flask.Flask(__name__)


@app.route("/", methods=["POST"])
def rating():
    data = request.get_json()
    value = handle_json_data(data)
    return jsonify(value)


app.run()
