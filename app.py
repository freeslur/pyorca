import pprint

from flask import Flask, jsonify, request
from flask_cors import CORS

from orcalib import patient, system_info

app = Flask(__name__)
app.config["JSON_AS_ASCII"] = False
CORS(app)


@app.route("/api/sys_info", methods=["GET"])
def sys_info():
    return jsonify(system_info.result)
    # return template_rendered("index.html", system_info=systeminfo.result)


@app.route("/api/patient_basic_info", methods=["GET"])
def patient_basic_info():
    res = patient.info("00012")
    if res["Api_Result"] == "10":
        return res["Api_Result_Message"]
    return jsonify(res["Patient_Information"])


@app.route("/api/delete_patient", methods=["POST"])
def delete_patient():
    res_data = patient.delete(request.json)
    pprint.pprint(res_data.decode("utf-8"))
    return res_data


@app.route("/api/regist_patient", methods=["POST"])
def regist_patient():
    res_data = patient.regist(request.json)
    pprint.pprint(res_data.decode("utf-8"))
    return res_data


if __name__ == "__main__":
    app.debug = True
    app.run(host="0.0.0.0", port=5000)
