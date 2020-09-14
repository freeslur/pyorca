from flask import Blueprint, jsonify, make_response

from serve.models.acceptance import Acceptance, AcceptanceSchema

acceptance_router = Blueprint("acceptance_router", __name__)


@acceptance_router.route("acceptances", methods=["GET"])
def getAcceptanceList():
    acceptances = Acceptance.getList()
    acceptance_schema = AcceptanceSchema(many=True)

    return make_response(
        jsonify({"code": 200, "acceptances": acceptance_schema.dump(acceptances).data})
    )


@acceptance_router.route("atest", methods=["GET"])
def getATest():
    patients = Acceptance.check()
    return patients


def registAcceptance():
    pass
