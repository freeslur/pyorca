import json

import requests
import xmltodict

import orcalib.orca_default as orca
from orcalib.orpatient import ORPatient
from orcalib.utils import json_to_post, res_to_json


class ORAcceptance:
    def __init__(self):
        self.pati = ORPatient()

    def list_all():
        # req_data = request_data["data"]
        post_data = orca.post_param_default(
            "acceptlstreq",
            (
                "<Acceptance_Date type='string'>2020-09-15</Acceptance_Date>"
                + "<Department_Code type='string'></Department_Code>"
                + "<Physician_Code type='string'></Physician_Code>"
                + "<Medical_Information type='string'></Medical_Information>"
                + "<Display_Order_Sort type='string'>True</Display_Order_Sort>"
            ),
        )

        result_list = []
        error = []

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
                    error.append("00")
            else:
                error.append(
                    json_data["Api_Result"] + " : " + json_data["Api_Result_Message"]
                )

        error_msg = ""
        for e in error:
            if e != "00":
                error_msg += e + "\n"

        result = {"data": result_list, "error": error_msg}
        return result

    def cancel(acc_date, acc_id, pati_id):
        post_data = orca.post_param_default(
            "acceptreq",
            json_to_post(
                {
                    "Request_Number": "02",
                    "Acceptance_Date": acc_date,
                    "Acceptance_Id": acc_id,
                    "Patient_ID": pati_id,
                }
            ),
        )
        print(post_data)

        result_list = []
        error = []

        res_data_accepted = xmltodict.parse(
            requests.post(
                url=orca.default_url + orca.acceptance_cancel,
                data=post_data.encode("utf-8"),
                headers=orca.post_headers,
                auth=orca.auth,
            ).content
        )
        json_data = res_to_json(
            dict(json.loads(json.dumps(res_data_accepted)))["xmlio2"]["acceptres"]
        )
        print(json_data)
        # if json_data["Api_Result"] == "00":
        #     acc_date = json_data["Acceptance_Date"]
        #     for data in json_data["Acceptlst_Information"]:
        #         acc_data = {
        #             "Acceptance_ID": data["Acceptance_Id"],
        #             "Acceptance_Date": acc_date,
        #             "Acceptance_Time": data["Acceptance_Time"],
        #             "Status": str(class_num),
        #             "Patient_Information": data["Patient_Information"],
        #             "InsuranceProvider_WholeName": data["HealthInsurance_Information"][
        #                 "InsuranceProvider_WholeName"
        #             ],
        #             "Department_WholeName": data["Department_WholeName"],
        #             "Physician_WholeName": data["Physician_WholeName"],
        #             "Patient_Memo": "",
        #             "Acceptance_Memo": "",
        #         }
        #         result_list.append(acc_data)
        #         error.append("00")
        # else:
        #     error.append(
        #         json_data["Api_Result"] + " : " + json_data["Api_Result_Message"]
        #     )

        result = {"data": result_list, "error": error}
        return result
