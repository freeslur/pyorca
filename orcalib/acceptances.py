import json
import pprint
from datetime import date

import requests
import xmltodict

import orcalib.orca_default as orca
from orcalib.orca_formatter import res_to_json


def calc_age(birth_date):
    ymd = birth_date.split("-")
    today = date.today()
    age = (
        today.year
        - int(ymd[0])
        - ((today.month, today.day) < (int(ymd[1]), int(ymd[2])))
    )
    return str(age) + "才"


def get_prev_acceptance_date(patient):

    return "2001-09-09"


def list_all():
    # req_data = request_data["data"]
    post_data = orca.post_param_default(
        "acceptlstreq",
        (
            "<Acceptance_Date type='string'>2020-09-10</Acceptance_Date>"
            + "<Department_Code type='string'></Department_Code>"
            + "<Physician_Code type='string'></Physician_Code>"
            + "<Medical_Information type='string'></Medical_Information>"
            + "<Display_Order_Sort type='string'>True</Display_Order_Sort>"
        ),
    )

    result_list = []

    for class_num in reversed(range(2)):
        res_data_accepted = xmltodict.parse(
            requests.post(
                url=orca.default_url + orca.acceptance_info(class_num=class_num + 1),
                data=post_data.encode("utf-8"),
                headers=orca.post_headers,
                auth=orca.auth,
            ).content
        )
        json_data = res_to_json(
            dict(json.loads(json.dumps(res_data_accepted)))["xmlio2"]["acceptlstres"][
                "Acceptlst_Information"
            ]
        )
        for data in json_data:
            acc_data = {
                "Acceptance_ID": data["Acceptance_Id"],
                "Acceptance_Time": data["Acceptance_Time"],
                "Status": str(class_num),
                "Patient_ID": data["Patient_Information"]["Patient_ID"],
                "WholeName_inKana": data["Patient_Information"]["WholeName_inKana"],
                "WholeName": data["Patient_Information"]["WholeName"],
                "BirthDate": calc_age(data["Patient_Information"]["BirthDate"]),
                "Sex": "男" if data["Patient_Information"]["Sex"] == "1" else "女",
                "InsuranceProvider_WholeName": data["HealthInsurance_Information"][
                    "InsuranceProvider_WholeName"
                ],
                "Department_WholeName": data["Department_WholeName"],
                "Physician_WholeName": data["Physician_WholeName"],
                "Previouse_Acceptance_Date": "",
                "Patient_Memo": "",
                "Acceptance_Memo": "",
            }
            result_list.append(acc_data)

    result = {"data": result_list}
    return result


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
