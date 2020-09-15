import json

import requests
import xmltodict

import orcalib.orca_default as orca
from orcalib.utils import check_new, json_to_post, res_to_json


class ORPatient:
    def __init__(self):
        pass

    def getInfo(self, patient_id):
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

    def get_prev_date(self, patient_id):
        patient_data = self.getInfo(patient_id=patient_id)
        return patient_data["Patient_Information"]["LastVisit_Date"]

    def get_memo(self, patient_id):
        print("go memo =================================")
        post_data = orca.post_param_default(
            "patientlst7req", json_to_post({"Patient_ID": "00001", "Memo_Class": "2"})
        )
        result_list = []
        error = ""

        res_data_newbie = xmltodict.parse(
            requests.post(
                url=orca.default_url + orca.patient_memo,
                data=post_data.encode("utf-8"),
                headers=orca.post_headers,
                auth=orca.auth,
            ).content
        )
        json_data = res_to_json(
            dict(json.loads(json.dumps(res_data_newbie)))["xmlio2"]["patientlst7res"]
        )
        print("=========json=========\n", json_data)
        if json_data["Api_Result"] == "00":
            print(len(json_data))
            # for data in json_data["Patient_Information"]:
            #     newbie_data = {
            #         "Patient_ID": data["Patient_ID"],
            #         "WholeName_inKana": data["WholeName_inKana"],
            #         "WholeName": data["WholeName"],
            #         "BirthDate": data["BirthDate"],
            #         "Sex": "男" if data["Sex"] == "1" else "女",
            #         "CreateDate": data["CreateDate"],
            #         "UpdateDate": data["UpdateDate"],
            #         "UpdateTime": data["UpdateTime"],
            #         "IsNew": check_new(
            #             data["CreateDate"], data["UpdateDate"], data["UpdateTime"]
            #         ),
            #     }
            #     result_list.append(newbie_data)
        else:
            error = json_data["Api_Result"] + " : " + json_data["Api_Result_Message"]

        result = {"error": error, "data": result_list}
        print(result)
        return "result"

    def getNewbies(params):
        post_data = orca.post_param_default("patientlst1req", json_to_post(params))
        result_list = []
        error = ""

        res_data_newbie = xmltodict.parse(
            requests.post(
                url=orca.default_url + orca.patient_newbie,
                data=post_data.encode("utf-8"),
                headers=orca.post_headers,
                auth=orca.auth,
            ).content
        )
        json_data = res_to_json(
            dict(json.loads(json.dumps(res_data_newbie)))["xmlio2"]["patientlst1res"]
        )
        if json_data["Api_Result"] == "00":
            print(len(json_data))
            for data in json_data["Patient_Information"]:
                newbie_data = {
                    "Patient_ID": data["Patient_ID"],
                    "WholeName_inKana": data["WholeName_inKana"],
                    "WholeName": data["WholeName"],
                    "BirthDate": data["BirthDate"],
                    "Sex": "男" if data["Sex"] == "1" else "女",
                    "CreateDate": data["CreateDate"],
                    "UpdateDate": data["UpdateDate"],
                    "UpdateTime": data["UpdateTime"],
                    "IsNew": check_new(
                        data["CreateDate"], data["UpdateDate"], data["UpdateTime"]
                    ),
                }
                result_list.append(newbie_data)
        else:
            error = json_data["Api_Result"] + " : " + json_data["Api_Result_Message"]

        result = {"error": error, "data": result_list}
        print(result)
        return result

    def checks(self):
        return ""

    def regist(self, patient_id):
        return "res"
