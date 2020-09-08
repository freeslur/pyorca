import json
import pprint

import requests
import xmltodict

import orcalib.orca_default as orca
from orcalib.orca_formatter import res_to_json


def list():
    # req_data = request_data["data"]
    post_data = orca.post_param_default(
        "acceptlstreq",
        (
            "<Acceptance_Date type='string'>2020-09-08</Acceptance_Date>"
            + "<Department_Code type='string'>01</Department_Code>"
            + "<Physician_Code type='string'>10001</Physician_Code>"
            + "<Medical_Information type='string'></Medical_Information>"
            + "<Display_Order_Sort type='string'>True</Display_Order_Sort>"
        ),
    )
    res = requests.post(
        url=orca.default_url + orca.acceptance_all_list,
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
