import json
from datetime import date

import requests
import xmltodict

import orcalib.orca_default as orca
from orcalib.orpatient import ORPatient
from orcalib.utils import res_to_json


class ORAcceptance:
    def __init__(self):
        self.pati = ORPatient()

    def calc_age(self, birth_date):
        ymd = birth_date.split("-")
        today = date.today()
        age = (
            today.year
            - int(ymd[0])
            - ((today.month, today.day) < (int(ymd[1]), int(ymd[2])))
        )
        return str(age) + "才"

    def list_all():
        # req_data = request_data["data"]
        post_data = orca.post_param_default(
            "acceptlstreq",
            (
                "<Acceptance_Date type='string'>2020-09-14</Acceptance_Date>"
                + "<Department_Code type='string'></Department_Code>"
                + "<Physician_Code type='string'></Physician_Code>"
                + "<Medical_Information type='string'></Medical_Information>"
                + "<Display_Order_Sort type='string'>True</Display_Order_Sort>"
            ),
        )

        result_list = []
        error = "00"

        for class_num in reversed(range(2)):
            res_data_accepted = xmltodict.parse(
                requests.post(
                    url=orca.default_url
                    + orca.acceptance_info(class_num=class_num + 1),
                    data=post_data.encode("utf-8"),
                    headers=orca.post_headers,
                    auth=orca.auth,
                ).content
            )
            json_data = res_to_json(
                dict(json.loads(json.dumps(res_data_accepted)))["xmlio2"][
                    "acceptlstres"
                ]
            )
            if json_data["Api_Result"] == "00":
                acc_date = json_data["Acceptance_Date"]
                for data in json_data["Acceptlst_Information"]:
                    acc_data = {
                        "Acceptance_ID": data["Acceptance_Id"],
                        "Acceptance_Date": acc_date,
                        "Acceptance_Time": data["Acceptance_Time"],
                        "Status": str(class_num),
                        "Patient_Information": data["Patient_Information"],
                        "InsuranceProvider_WholeName": data[
                            "HealthInsurance_Information"
                        ]["InsuranceProvider_WholeName"],
                        "Department_WholeName": data["Department_WholeName"],
                        "Physician_WholeName": data["Physician_WholeName"],
                        "Patient_Memo": "",
                        "Acceptance_Memo": "",
                    }
                    result_list.append(acc_data)
            else:
                error = (
                    json_data["Api_Result"] + " : " + json_data["Api_Result_Message"]
                )

        result = {"data": result_list, "error": error}
        return result

    def cancel(self):
        self.pati.checks()
        self.pati.regist()
        return ""
