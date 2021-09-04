from datetime import datetime

from flask import Blueprint
from flask.json import jsonify

from han_port.han_port_data import get_han_data
from nilm.nilm import get_applience_consumption

distrobution = Blueprint("distrobution", __name__)


@distrobution.get("/")
def get_distrobution():
    detail_data = get_han_data()

    from_date = datetime.strptime(detail_data[0][1], "%Y-%m-%dT%H:%M:%S")
    to_date = datetime.strptime(detail_data[-1][1], "%Y-%m-%dT%H:%M:%S")

    split = get_applience_consumption(from_date, to_date, detail_data)

    return jsonify(split.as_json())
