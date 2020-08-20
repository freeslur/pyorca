import requests
import xmltodict

import orcalib.orca_default as orca

import pprint

result = xmltodict.parse(
    requests.get(
        url=orca.default_url + orca.patient_basic_info + "id=00000",
        auth=orca.auth,
    ).content
)["xmlio2"]["patientinfores"]


def delete(request_data):
    pprint.pprint(request_data)
    req_data = request_data["data"]
    pprint.pprint(req_data["name"])
    post_data = orca.post_param_default("patientmodreq",
                                        ("<Patient_ID type='string'>"+req_data["id"]+"</Patient_ID>"
                                         "<WholeName type='string'>" +
                                         req_data["name"]+"</WholeName>"
                                         "<WholeName_inKana type='string'>" +
                                         req_data["name_kana"] +
                                         "</WholeName_inKana>"
                                         "<BirthDate type='string'>" +
                                         req_data["birth_date"]+"</BirthDate>"
                                         "<Sex type='string'>"+req_data["sex"]+"</Sex>")
                                        )
    return requests.post(
        url=orca.default_url + orca.delete_patient,
        data=post_data,
        headers=orca.post_headers,
        auth=orca.auth
    ).content
