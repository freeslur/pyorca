from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
from orcalib import system_info, patient

import pprint

app = Flask(__name__)
app.config["JSON_AS_ASCII"] = False
CORS(app)


@app.route("/api/sys_info", methods=["GET"])
def sys_info():
    return jsonify(system_info.result)
    # return template_rendered("index.html", system_info=systeminfo.result)


@app.route("/api/patient_basic_info", methods=["GET"])
# @cross_origin(methods=["GET"])
def patient_basic_info():
    return jsonify(patient.result["Patient_Information"])


@app.route("/api/delete_patient", methods=["POST"])
# @cross_origin(allow_headers="*", origins="*", methods=["GET", "HEAD", "POST", "OPTIONS", "PUT", "PATCH", "DELETE"])
def delete_patient():
    return patient.delete(request.json)


if __name__ == "__main__":
    app.debug = True
    app.run(host="0.0.0.0", port=5000)
