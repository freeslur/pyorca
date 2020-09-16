import orcalib.or_default as orca
from orcalib.or_patient import ORPatient
from orcalib.or_utils import json_to_post, post_request


class ORAcceptance:
    def __init__(self, selected_date):
        self.selected_date = selected_date
        self.pati = ORPatient()

    def list_all(self):
        post_data = orca.post_param_wrapper(
            "acceptlstreq",
            json_to_post({"Acceptance_Date": self.selected_date}),
        )

        results = []
        error = []

        for class_num in reversed(range(2)):
            json_data = post_request(
                api_uri=orca.acceptance_info(class_num=class_num + 1),
                res_key="acceptlstres",
                post_data=post_data,
            )
            print(json_data)
            if json_data["Api_Result"] == "00":
                acc_date = json_data["Acceptance_Date"]
                for data in json_data["Acceptlst_Information"]:
                    acc_data = {
                        "Acceptance_ID": data["Acceptance_Id"],
                        "Acceptance_Date": acc_date,
                        "Acceptance_Time": data["Acceptance_Time"],
                        "Status": str(class_num + 1)
                        if class_num == 1
                        else str(class_num),
                        "Patient_Information": data["Patient_Information"],
                        "InsuranceProvider_WholeName": data[
                            "HealthInsurance_Information"
                        ]["InsuranceProvider_WholeName"]
                        if "HealthInsurance_Information" in data.keys()
                        else "",
                        "Department_WholeName": data["Department_WholeName"],
                        "Physician_WholeName": data["Physician_WholeName"],
                        "Patient_Memo": "",
                        "Acceptance_Memo": "",
                        "BigData": data,
                    }
                    results.append(acc_data)
                    error.append("00")
            else:
                error.append(
                    json_data["Api_Result"] + " : " + json_data["Api_Result_Message"]
                )

        error_msg = ""
        for e in error:
            if e != "00":
                error_msg += e + "\n"

        result = {"data": results, "error": error_msg}
        return result

    def cancel(self, acc_time, acc_id, pati_id):
        post_data = orca.post_param_default(
            "acceptreq",
            json_to_post(
                {
                    "Request_Number": "02",
                    "Acceptance_Date": self.selected_date,
                    "Acceptance_Time": acc_time,
                    "Acceptance_Id": acc_id,
                    "Patient_ID": pati_id,
                }
            ),
        )

        result = {}
        error = ""

        json_data = post_request(
            api_uri=orca.acceptance_cancel, res_key="acceptres", post_data=post_data
        )
        if json_data["Api_Result"] == "K3":
            result = json_data
            error = "K3"
        else:
            error = json_data["Api_Result"] + " : " + json_data["Api_Result_Message"]

        result = {"data": json_data, "error": error}
        return result

    def send_receipt(data):
        # post_data = orca.post_param_default(
        #     "medicalreq",
        #     json_to_post(
        #         {
        #             "Request_Number": "02",
        #             "Acceptance_Date": acc_date,
        #             "Acceptance_Time": acc_time,
        #             "Acceptance_Id": acc_id,
        #             "Patient_ID": pati_id,
        #         }
        #     ),
        # )
        # print(post_data)
        print("=========================")
        print(data)
        print("=========================")

        result = {}
        error = ""

        # res_data_accepted = xmltodict.parse(
        #     requests.post(
        #         url=orca.default_url + orca.acceptance_cancel,
        #         data=post_data.encode("utf-8"),
        #         headers=orca.post_headers,
        #         auth=orca.auth,
        #     ).content
        # )
        # json_data = res_to_json(
        #     dict(json.loads(json.dumps(res_data_accepted)))["xmlio2"]["medicalres"]
        # )
        # print(json_data)
        # if json_data["Api_Result"] == "K3":
        #     result = json_data
        #     error = "K3"
        # else:
        #     error = json_data["Api_Result"] + " : " + json_data["Api_Result_Message"]

        result = {"data": "json_data", "error": error}
        return result
