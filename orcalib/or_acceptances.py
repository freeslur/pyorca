import orcalib.or_default as orca
from orcalib.or_patient import ORPatient
from orcalib.or_utils import post_request, req_to_xml


class ORAcceptance:
    def __init__(self, acc_date):
        self.acc_date = acc_date

    def list_all(self):
        post_data = req_to_xml(
            "acceptlstreq", req_data={"Acceptance_Date": self.acc_date}
        )

        results = []
        error = []

        for class_num in reversed(range(2)):
            json_data = post_request(
                api_uri=orca.acceptance_info(class_num=class_num + 1),
                res_key="acceptlstres",
                post_data=post_data,
            )
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
                        "InsuranceProvider_WholeName": (
                            data["HealthInsurance_Information"][
                                "InsuranceProvider_WholeName"
                            ]
                            if "InsuranceProvider_WholeName"
                            in data["HealthInsurance_Information"].keys()
                            else ""
                        )
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
        post_data = req_to_xml(
            req_key="acceptreq",
            req_data={
                "Request_Number": "02",
                "Acceptance_Date": self.acc_date,
                "Acceptance_Time": acc_time,
                "Acceptance_Id": acc_id,
                "Patient_ID": pati_id,
            },
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
        data_default = data["default"]
        data_perform = data["perform"]
        data_medical = data["medical"]
        p_data = {
            "Patient_ID": data_default["Patient_Information"]["Patient_ID"],
            "Perform_Date": data_perform["Perform_Date"],
            "Perform_Time": data_perform["Perform_Time"],
            "Diagnosis_Information": {
                "Department_Code": data_default["Department_Code"],
                "Physician_Code": data_default["Physician_Code"],
                "HealthInsurance_Information": data_default[
                    "HealthInsurance_Information"
                ],
                "Medical_Information": data_medical["Medical_Information"],
                "Disease_Information": data_medical["Disease_Information"],
            },
        }
        post_data = req_to_xml(req_key="medicalreq", req_data=p_data)

        result = {}
        error = ""

        json_data = post_request(
            api_uri=orca.regist_receipt, res_key="medicalres", post_data=post_data
        )
        if json_data["Api_Result"] == "00":
            result = json_data
            error = "00"
        else:
            error = json_data["Api_Result"] + " : " + json_data["Api_Result_Message"]

        result = {"data": json_data, "error": error}
        return result


class ORAcceptance2:
    def __init__(self, acc_date):
        self.acc_date = acc_date
        self.pati = ORPatient()

    def list_all(self):
        post_data = req_to_xml(
            "acceptlstreq", req_data={"Acceptance_Date": self.acc_date}
        )

        results = []
        error = []

        for class_num in reversed(range(2)):
            json_data = post_request(
                api_uri=orca.acceptance_info(class_num=class_num + 1),
                res_key="acceptlstres",
                post_data=post_data,
            )
            if json_data["Api_Result"] == "00":
                for data in json_data["Acceptlst_Information"]:
                    acc_data = {
                        "Acceptance_ID": data["Acceptance_Id"],
                        "Acceptance_Date": self.acc_date,
                        "Acceptance_Time": data["Acceptance_Time"],
                        "Status": str(class_num + 1)
                        if class_num == 1
                        else str(class_num),
                        "Patient_Information": data["Patient_Information"],
                        "InsuranceProvider_WholeName": (
                            data["HealthInsurance_Information"][
                                "InsuranceProvider_WholeName"
                            ]
                            if "InsuranceProvider_WholeName"
                            in data["HealthInsurance_Information"].keys()
                            else ""
                        )
                        if "HealthInsurance_Information" in data.keys()
                        else "",
                        "Department_WholeName": data["Department_WholeName"],
                        "Physician_WholeName": data["Physician_WholeName"],
                        "Acceptance_Memo": "",
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
        post_data = req_to_xml(
            req_key="acceptreq",
            req_data={
                "Request_Number": "02",
                "Acceptance_Date": self.selected_date,
                "Acceptance_Time": acc_time,
                "Acceptance_Id": acc_id,
                "Patient_ID": pati_id,
            },
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
        data_default = data["default"]
        data_perform = data["perform"]
        data_medical = data["medical"]
        p_data = {
            "Patient_ID": data_default["Patient_Information"]["Patient_ID"],
            "Perform_Date": data_perform["Perform_Date"],
            "Perform_Time": data_perform["Perform_Time"],
            "Diagnosis_Information": {
                "Department_Code": data_default["Department_Code"],
                "Physician_Code": data_default["Physician_Code"],
                "HealthInsurance_Information": data_default[
                    "HealthInsurance_Information"
                ],
                "Medical_Information": data_medical["Medical_Information"],
                "Disease_Information": data_medical["Disease_Information"],
            },
        }
        post_data = req_to_xml(req_key="medicalreq", req_data=p_data)

        result = {}
        error = ""

        json_data = post_request(
            api_uri=orca.regist_receipt, res_key="medicalres", post_data=post_data
        )
        if json_data["Api_Result"] == "00":
            result = json_data
            error = "00"
        else:
            error = json_data["Api_Result"] + " : " + json_data["Api_Result_Message"]

        result = {"data": json_data, "error": error}
        return result
