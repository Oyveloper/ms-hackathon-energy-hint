from flask import Blueprint
from flask.json import jsonify

from advice.advice_generator import get_all_advice_for_device

advice = Blueprint("advice", __name__)


@advice.route("/<device>", methods=["GET"])
def get_advice(device):
    return jsonify(tuple(map(lambda x: x.as_dict(), get_all_advice_for_device(device))))
