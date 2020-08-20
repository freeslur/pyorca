default_url = "http://localhost:8000"
system_info = "/api01rv2/systeminfv2"
patient_basic_info = "/api01rv2/patientgetv2?"
regist_patient = "/orca12/patientmodv2?class=01"
update_patient = "/orca12/patientmodv2?class=02"
delete_patient = "/orca12/patientmodv2?class=03"
post_headers = {"Content-Type": "application/xml"}
auth = ("ormaster", "ormaster")


def post_param_default(api_key, param_string):
    return "<data><"+api_key+" type='record'>"+param_string+"</"+api_key+"></data>"


def get_param_default(params):
    return params
