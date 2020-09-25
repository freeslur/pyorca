default_url = "http://trial.orca.med.or.jp:8000"
system_info = "/api01rv2/systeminfv2"
patient_basic_info = "/api01rv2/patientgetv2?"
patient_newbie = "/api01rv2/patientlst1v2?class=01"
patient_memo = "/api01rv2/patientlst7v2"
regist_patient = "/orca12/patientmodv2?class=01"
update_patient = "/orca12/patientmodv2?class=02"
delete_patient = "/orca12/patientmodv2?class=03"
acceptance_all_list = "/api01rv2/acceptlstv2?class=03"
acceptance_cancel = "/orca11/acceptmodv2"
regist_receipt = "/api21/medicalmodv2?class=01"
post_headers = {"Content-Type": "application/xml"}
auth = ("trial", "")


def acceptance_info(class_num):
    return "/api01rv2/acceptlstv2?class=0" + str(class_num)


def get_param_default(params):
    return params
