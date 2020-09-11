import json
import pprint

import requests
import xmltodict

import orcalib.orca_default as orca
from orcalib.orca_formatter import res_to_json


def patient_info(patient_id):
    ordered_dict_data = xmltodict.parse(
        requests.get(
            url=orca.default_url + orca.patient_basic_info + "id=" + patient_id,
            auth=orca.auth,
        ).content
    )
    json_data = dict(json.loads(json.dumps(ordered_dict_data)))["xmlio2"][
        "patientinfores"
    ]
    result = res_to_json(json_data)
    return result


def delete(request_data):
    pprint.pprint(request_data)
    req_data = request_data["data"]
    pprint.pprint(req_data)
    post_data = orca.post_param_default(
        "patientmodreq",
        (
            "<Patient_ID type='string'>" + req_data["id"] + "</Patient_ID>"
            "<WholeName type='string'>" + req_data["name"] + "</WholeName>"
            "<WholeName_inKana type='string'>"
            + req_data["name_kana"]
            + "</WholeName_inKana>"
            "<BirthDate type='string'>" + req_data["birth_date"] + "</BirthDate>"
            "<Sex type='string'>" + req_data["sex"] + "</Sex>"
        ),
    )
    res = requests.post(
        url=orca.default_url + orca.delete_patient,
        data=post_data.encode("utf-8"),
        headers=orca.post_headers,
        auth=orca.auth,
    ).content
    pprint.pprint("OK??")
    return res


def newbie(request_data):
    req_data = request_data["data"]
    pprint.pprint(req_data)


def regist(request_data):
    req_data = request_data["data"]
    pprint.pprint(req_data)
    post_data = orca.post_param_default(
        "patientmodreq",
        (
            "<Patient_ID type='string'>" + req_data["id"] + "</Patient_ID>"
            "<WholeName type='string'>" + req_data["name"] + "</WholeName>"
            "<WholeName_inKana type='string'>"
            + req_data["name_kana"]
            + "</WholeName_inKana>"
            "<BirthDate type='string'>" + req_data["birth_date"] + "</BirthDate>"
            "<Sex type='string'>" + req_data["sex"] + "</Sex>"
        ),
    )
    res = requests.post(
        url=orca.default_url + orca.regist_patient,
        data=post_data.encode("utf-8"),
        headers=orca.post_headers,
        auth=orca.auth,
    ).content
    pprint.pprint("OK??")
    return res
