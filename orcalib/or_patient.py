import orcalib.or_default as orca
from orcalib.or_utils import get_request


class ORPatient:
    def __init__(self, pati_id):
        self.pati_id = pati_id

    def get_info(self):
        result = get_request(
            api_uri=orca.patient_basic_info,
            res_key="patientinfores",
            params="id=" + self.pati_id,
        )
        return result

    def get_prev_date(self):
        patient_data = self.get_info()
        result = (
            patient_data["Patient_Information"]["LastVisit_Date"]
            if "LastVisit_Date" in patient_data["Patient_Information"].keys()
            else "初診"
        )
        return result

    def checks(self):
        return ""

    def regist(self):
        return "res"
