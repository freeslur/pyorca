import pprint

import orcalib.orca_default as orca
import requests
from orcalib.orca_formatter import res_to_json


def info(patient_id):
    result = res_to_json(
        requests.get(
            url=orca.default_url + orca.patient_basic_info + "id=" + patient_id,
            auth=orca.auth,
        ).content,
        "patientinfores",
    )
    return result


def delete(request_data):
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
    res = requests.delete(
        url=orca.default_url + orca.delete_patient,
        data=post_data.encode("utf-8"),
        headers=orca.post_headers,
        auth=orca.auth,
    ).content
    pprint.pprint("OK??")
    return res
    # return requests.post(
    #     url=orca.default_url + orca.delete_patient,
    #     data=post_data.encode("utf-8"),
    #     headers=orca.post_headers,
    #     auth=orca.auth
    # ).content


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
