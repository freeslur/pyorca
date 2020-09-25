import config
from flask import Blueprint, jsonify, make_response, request
from orcalib.or_default import acceptance_info
from orcalib.or_patient import ORPatient
from orcalib.or_utils import calc_age
from serve.data_cache.MAcceptance import get_or_acc_data

# from serve.models.m_acceptance import Acceptance, AcceptanceSchema
# from serve.models.m_patient import PatientSchema

acceptance_router = Blueprint("acceptance_router", __name__)


def get_acc_datas():
    acceptances = get_or_acc_data()["data"]
    data = []
    for acc in acceptances:
        d1 = acc
        d2 = acc["Patient_Information"]
        d1["Patient_ID"] = d2["Patient_ID"]
        d1["WholeName_inKana"] = d2["WholeName_inKana"]
        d1["WholeName"] = d2["WholeName"]
        d1["BirthDate"] = calc_age(d2["BirthDate"])
        d1["Sex"] = "男" if d2["Sex"] == "1" else "女"
        orp = ORPatient(pati_id=d1["Patient_ID"])
        d1["LastVisit_Date"] = orp.get_prev_date()
        data.append(d1)
    return data


@acceptance_router.route("acceptances", methods=["POST"])
def get_acceptance_list():
    config.acc_date = request.get_json()["acceptance_date"]
    return make_response(jsonify(get_acc_datas()))


@acceptance_router.route("acc_date/<date>", methods=["GET"])
def set_acc_date(date=None):
    config.acc_date = date
    return {"code": 200, "data": {}}


@acceptance_router.route("acceptances/send", methods=["POST"])
def get_receipt_data_f():
    data = request.get_json()
    data_big = data["default"]["BigData"]
    data["default"] = data_big
    acceptance_info.send_receipt(data)

    return make_response(jsonify(data))
