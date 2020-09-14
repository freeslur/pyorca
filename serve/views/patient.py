from flask import Blueprint, jsonify, make_response

from serve.models.patient import Patient, PatientSchema

patient_router = Blueprint("patient_router", __name__)


@patient_router.route("patients", methods=["GET"])
def getPatientList():
    patients = Patient.getPatientList()
    patient_schema = PatientSchema(many=True)

    return make_response(
        jsonify({"code": 200, "patients": patient_schema.dump(patients).data})
    )


@patient_router.route("ptest", methods=["GET"])
def getTest():
    patients = Patient.getNewbie()
    return patients


def registPatient():
    pass
