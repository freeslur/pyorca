from flask import Blueprint, jsonify, make_response, request
from orcalib.or_patient import ORPatient

patient_router = Blueprint("patient_router", __name__)


@patient_router.route("patient", methods=["GET"])
def get_patient():
    pati_id = request.args.get("id")
    print(pati_id)
    orp = ORPatient(pati_id=pati_id)
    pati = orp.get_info()
    return make_response(jsonify(pati))
