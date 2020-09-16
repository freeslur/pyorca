from flask import Blueprint, jsonify, make_response

from serve.models.m_patient import Patient, PatientSchema

patient_router = Blueprint("patient_router", __name__)


@patient_router.route("patients", methods=["GET"])
def get_patient_list():
    patients = Patient.get_patient_list()
    patient_schema = PatientSchema(many=True)

    return make_response(
        jsonify({"code": 200, "patients": patient_schema.dump(patients).data})
    )


@patient_router.route("ptest", methods=["GET"])
def getTest():
    pass


@patient_router.route("pclear", methods=["GET"])
def getClear():
    patients = Patient.clear()
    return patients


def registPatient():
    pass
