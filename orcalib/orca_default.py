default_url = "http://trial.orca.med.or.jp:8000"
# default_url = "http://localhost:8000"
system_info = "/api01rv2/systeminfv2"
patient_basic_info = "/api01rv2/patientgetv2?"
patinet_newbie = "/api01rv2/patientlst1v2?class=01"
regist_patient = "/orca12/patientmodv2?class=01"
update_patient = "/orca12/patientmodv2?class=02"
delete_patient = "/orca12/patientmodv2?class=03"
acceptance_all_list = "/api01rv2/acceptlstv2?class=03"
post_headers = {"Content-Type": "application/xml"}
auth = ("trial", "")
# auth = ("ormaster", "ormaster")


def acceptance_info(class_num):
    return "/api01rv2/acceptlstv2?class=0" + str(class_num)


def post_param_default(api_key, param_string):
    return (
        "<data><"
        + api_key
        + " type='record'>"
        + param_string
        + "</"
        + api_key
        + "></data>"
    )


def get_param_default(params):
    return params
