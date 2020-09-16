import orcalib.or_default as orca
from orcalib.or_utils import get_request


class ORPatient:
    def __init__(self):
        pass

    def get_info(patient_id):
        result = get_request(
            api_uri=orca.patient_basic_info,
            res_key="patientinfores",
            params="id=" + patient_id,
        )
        return result

    def get_prev_date(self, patient_id):
        patient_data = self.get_info(patient_id=patient_id)
        return patient_data["Patient_Information"]["LastVisit_Date"]

    def checks(self):
        return ""

    def regist(self, patient_id):
        return "res"
