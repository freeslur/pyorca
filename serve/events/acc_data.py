import json

import config
from orcalib.or_acceptances import ORAcceptance
from orcalib.or_patient import ORPatient
from serve.database import db
from serve.models.m_acceptance import Acceptance
from serve.models.m_patient import Patient


def check(selected_date):
    or_data = {}
    or_acc = ORAcceptance(selected_date=selected_date)
    or_data = or_acc.list_all()
    if len(or_data["data"]) > 0:
        for o_d in or_data["data"]:
            if (
                "Patient_Information" in o_d.keys()
                and "Patient_ID" in o_d["Patient_Information"].keys()
            ):
                p_id = o_d["Patient_Information"]["Patient_ID"]
                acc_id = o_d["Acceptance_ID"]

                #             # Patient Add & Update
                #             # orp = ORPatient()
                last_visit_date = ORPatient.get_prev_date(ORPatient, patient_id=p_id)
                # pati = Patient(
                #     Patient_ID=p_id,
                #     WholeName=o_d["Patient_Information"]["WholeName"],
                #     WholeName_inKana=o_d["Patient_Information"]["WholeName_inKana"],
                #     BirthDate=o_d["Patient_Information"]["BirthDate"],
                #     Sex=o_d["Patient_Information"]["Sex"],
                #     LastVisit_Date=last_visit_date,
                #     Patient_Memo="",
                # )
                # if Patient.is_patient(Patient, p_id):
                #     db.session.merge(pati)
                # else:
                #     db.session.add(pati)
                # db.session.commit()

                #             # Acceptance Add & Update
                acc = Acceptance(
                    Acceptance_ID=acc_id,
                    Acceptance_Date=o_d["Acceptance_Date"],
                    Acceptance_Time=o_d["Acceptance_Time"],
                    Status=o_d["Status"],
                    Patient_ID=p_id,
                    InsuranceProvider_WholeName=o_d["InsuranceProvider_WholeName"],
                    Department_WholeName=o_d["Department_WholeName"],
                    Physician_WholeName=o_d["Physician_WholeName"],
                    BigData=json.dumps(o_d["BigData"]),
                )
    #             if Acceptance.is_acceptance(
    #                 selected_date=selected_date, acceptance_id=acc_id
    #             ):
    #                 db.session.merge(acc)
    #             else:
    #                 db.session.add(acc)
    #             db.session.commit()
    return or_data


def get_accs():
    data = check(config.acc_date)
    acceptances = Acceptance.get_list(selected_date=config.acc_date)
    acceptance_schema = AcceptanceSchema()
    patient_schema = PatientSchema()
    data = []
    for acc in acceptances:
        d1 = acceptance_schema.dump(acc[0])
        d2 = patient_schema.dump(acc[1])
        d1["WholeName_inKana"] = d2["WholeName_inKana"]
        d1["WholeName"] = d2["WholeName"]
        d1["BirthDate"] = calc_age(d2["BirthDate"])
        d1["Sex"] = "男" if d2["Sex"] == "1" else "女"
        d1["LastVisit_Date"] = d2["LastVisit_Date"]
        d1["Patient_Memo"] = d2["Patient_Memo"]
        data.append(d1)
    return data
