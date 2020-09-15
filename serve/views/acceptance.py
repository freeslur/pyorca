from flask import Blueprint, jsonify, make_response

from orcalib.utils import calc_age
from serve.models.acceptance import Acceptance, AcceptanceSchema
from serve.models.patient import PatientSchema

acceptance_router = Blueprint("acceptance_router", __name__)


@acceptance_router.route("acceptances", methods=["GET"])
def getAcceptanceList():
    Acceptance.check()
    acceptances = Acceptance.getList()
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
        d1["Patient_Memo"] = d2["Memo"]
        data.append(d1)

    return make_response(jsonify(data))


@acceptance_router.route("acceptances/cancel", methods=["GET"])
def getAcceptanceCancel():
    Acceptance.cancel("aaaa")
    Acceptance.check()
    acceptances = Acceptance.getList()
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
        d1["Patient_Memo"] = d2["Memo"]
        data.append(d1)

    return make_response(jsonify(data))


@acceptance_router.route("atest", methods=["GET"])
def getATest():
    patients = Acceptance.cancel()
    return patients


def registAcceptance():
    pass
