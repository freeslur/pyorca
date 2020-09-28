import config
from flask import Blueprint, jsonify, make_response, request
from orcalib.or_acceptances import ORAcceptance
from orcalib.or_patient import ORPatient
from orcalib.or_utils import calc_age
from serve.data_cache import database
from serve.data_cache.caching import (
    delete_acceptance,
    insert_acceptance,
    select_acceptance,
    update_acceptance,
)
from serve.data_cache.model.models import get_or_acc_data
from utils.diff import AccDiff

# from serve.models.m_acceptance import Acceptance, AcceptanceSchema
# from serve.models.m_patient import PatientSchema

acceptance_router = Blueprint("acceptance_router", __name__)


def get_acc_datas():
    acceptances = get_or_acc_data()["data"]
    data = []
    acc_data = []
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
        acc_data.append(
            {
                "Acceptance_Date": d1["Acceptance_Date"],
                "Acceptance_ID": d1["Acceptance_ID"],
                "Acceptance_Time": d1["Acceptance_Time"],
                "Status": int(d1["Status"]),
                "Patient_ID": d1["Patient_ID"],
            }
        )

    database.init()
    accdiff = AccDiff()

    prev = select_acceptance(acc_date=config.acc_date)
    accdiff.diff(prev, acc_data)
    if len(accdiff.added()):
        insert_acceptance(accdiff.added())
    if len(accdiff.changed()):
        update_acceptance(accdiff.changed())
    if len(accdiff.removed()):
        delete_acceptance(accdiff.removed())
    # nows = select_acceptance(acc_date=config.acc_date)

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
    ORAcceptance.send_receipt(data)

    return make_response(jsonify(data))


@acceptance_router.route("acceptances/cancel", methods=["POST"])
def cancel_receipt():
    data = request.get_json()
    ora = ORAcceptance(config.acc_date)
    ora.cancel(
        acc_time=data["acc_time"], acc_id=data["acc_id"], pati_id=data["pati_id"]
    )

    return make_response(jsonify(data))
