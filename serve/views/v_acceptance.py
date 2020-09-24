import json

from flask import Blueprint, jsonify, make_response, request

import config

# from app import socketio
from orcalib.or_utils import calc_age
from serve.models.m_acceptance import Acceptance, AcceptanceSchema
from serve.models.m_patient import PatientSchema

# from flask_socketio import emit


acceptance_router = Blueprint("acceptance_router", __name__)

# user_no = 1


# @acceptance_router.before_request
# def acc_befor_request():
#     global user_no
#     if "session" in session and "user-id" in session:
#         pass
#     else:
#         session["session"] = os.urandom(24)
#         session["username"] = "user" + str(user_no)
#         user_no += 1


def get_acc_datas():
    print("acc_date : ==========================", config.acc_date)
    Acceptance.check(selected_date=config.acc_date)
    acceptances = Acceptance.get_list(selected_date=config.acc_date)
    acceptance_schema = AcceptanceSchema()
    patient_schema = PatientSchema()
    data = []
    for acc in acceptances:
        d1 = acceptance_schema.dump(acc[0])
        d2 = patient_schema.dump(acc[1])
        d1["WholeName_inKana"] = d2["WholeName_inKana"]
        d1["WholeName"] = d2["WholeName"]
        d1["BirthDate"] = calc_age(d2["BirthDate"])
        d1["Sex"] = "男" if d2["Sex"] == "1" else "女"
        d1["LastVisit_Date"] = d2["LastVisit_Date"]
        d1["Patient_Memo"] = d2["Patient_Memo"]
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


@acceptance_router.route("acceptances/cancel", methods=["POST"])
def get_acceptance_cancel():
    data = request.get_json()
    Acceptance.cancel(
        selected_date=data["acc_date"],
        acceptance_id=data["acc_id"],
        acceptance_time=data["acc_time"],
        patient_id=data["pati_id"],
    )
    Acceptance.check(selected_date=data["acc_date"])
    acceptances = Acceptance.get_list(selected_date=data["acc_date"])
    acceptance_schema = AcceptanceSchema()
    patient_schema = PatientSchema()
    data = []
    for acc in acceptances:
        d1 = acceptance_schema.dump(acc[0])
        d2 = patient_schema.dump(acc[1])
        d1["WholeName_inKana"] = d2["WholeName_inKana"]
        d1["WholeName"] = d2["WholeName"]
        d1["BirthDate"] = calc_age(d2["BirthDate"])
        d1["Sex"] = "男" if d2["Sex"] == "1" else "女"
        d1["LastVisit_Date"] = d2["LastVisit_Date"]
        d1["Patient_Memo"] = d2["Patient_Memo"]
        data.append(d1)

    return make_response(jsonify(data))


@acceptance_router.route("acceptances/send", methods=["POST"])
def get_receipt_data_f():
    data = request.get_json()
    data_big = json.loads(data["default"]["BigData"])
    data["default"] = data_big
    Acceptance.get_receipt_data(data)

    return make_response(jsonify(data))


@acceptance_router.route("atest", methods=["GET"])
def getATest():
    patients = Acceptance.cancel(
        acceptance_id="00001",
        acceptance_time="01:31:19",
        patient_id="00011",
        selected_date="2020-09-16",
    )
    return patients


@acceptance_router.route("aclear", methods=["GET"])
def getClear():
    patients = Acceptance.clear()
    return patients


def registAcceptance():
    pass
