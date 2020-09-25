from flask import Blueprint, jsonify, make_response, request
from orcalib.or_patient import ORPatient

patient_router = Blueprint("patient_router", __name__)


@patient_router.route("patient", methods=["GET"])
def get_patient():
    pati_id = request.args.get("id")
    pati = ORPatient.get_info(patient_id=pati_id)
    return make_response(jsonify(pati))
