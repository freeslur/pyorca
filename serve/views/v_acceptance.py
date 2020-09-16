from flask import Blueprint, jsonify, make_response, request

from orcalib.or_utils import calc_age
from serve.models.m_acceptance import Acceptance, AcceptanceSchema
from serve.models.m_patient import PatientSchema

acceptance_router = Blueprint("acceptance_router", __name__)


@acceptance_router.route("acceptances", methods=["POST"])
def get_acceptance_list():
    date = request.get_json()["acceptance_date"]
    Acceptance.check(selected_date=date)
    acceptances = Acceptance.get_list(selected_date=date)
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
    Acceptance.get_receipt_data(data)
    # Acceptance.check(selected_date=data["acc_date"])
    # acceptances = Acceptance.getList(selected_date=data["acc_date"])
    # acceptance_schema = AcceptanceSchema()
    # patient_schema = PatientSchema()
    # data = []
    # for acc in acceptances:
    #     d1 = acceptance_schema.dump(acc[0])
    #     d2 = patient_schema.dump(acc[1])
    #     d1["WholeName_inKana"] = d2["WholeName_inKana"]
    #     d1["WholeName"] = d2["WholeName"]
    #     d1["BirthDate"] = calc_age(d2["BirthDate"])
    #     d1["Sex"] = "男" if d2["Sex"] == "1" else "女"
    #     d1["LastVisit_Date"] = d2["LastVisit_Date"]
    #     d1["Patient_Memo"] = d2["Memo"]
    #     data.append(d1)

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
