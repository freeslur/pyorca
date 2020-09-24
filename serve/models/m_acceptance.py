import json

from orcalib.or_acceptances import ORAcceptance
from orcalib.or_patient import ORPatient
from serve.database import db, ma
from serve.models.m_patient import Patient


class Acceptance(db.Model):
    __tablename__ = "acceptances"
    Acceptance_ID = db.Column(db.String(256), primary_key=True, nullable=False)
    Acceptance_Date = db.Column(db.String(256), primary_key=True, nullable=False)
    Acceptance_Time = db.Column(db.String(256), index=True, nullable=False)
    Status = db.Column(db.Integer, index=True, nullable=True)
    Patient_ID = db.Column(db.String(256), nullable=True)
    InsuranceProvider_WholeName = db.Column(db.String(256), nullable=True)
    Department_WholeName = db.Column(db.String(256), nullable=True)
    Physician_WholeName = db.Column(db.String(256), nullable=True)
    Patient_Memo = db.Column(db.String(256), nullable=True)
    Acceptance_Memo = db.Column(db.String(256), nullable=True)
    BigData = db.Column(db.Text(), nullable=True)

    def __repr__(self):
        return "<Acceptance %r>" % self.Acceptance_ID

    def __init__(
        self,
        Acceptance_ID,
        Acceptance_Date,
        Acceptance_Time,
        Status,
        Patient_ID,
        InsuranceProvider_WholeName,
        Department_WholeName,
        Physician_WholeName,
        BigData,
        Acceptance_Memo="",
    ):
        self.Acceptance_ID = Acceptance_ID
        self.Acceptance_Date = Acceptance_Date
        self.Acceptance_Time = Acceptance_Time
        self.Status = Status
        self.Patient_ID = Patient_ID
        self.InsuranceProvider_WholeName = InsuranceProvider_WholeName
        self.Department_WholeName = Department_WholeName
        self.Physician_WholeName = Physician_WholeName
        self.Acceptance_Memo = Acceptance_Memo
        self.BigData = BigData

    def check(selected_date):
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

                    # Patient Add & Update
                    # orp = ORPatient()
                    last_visit_date = ORPatient.get_prev_date(
                        ORPatient, patient_id=p_id
                    )
                    pati = Patient(
                        Patient_ID=p_id,
                        WholeName=o_d["Patient_Information"]["WholeName"],
                        WholeName_inKana=o_d["Patient_Information"]["WholeName_inKana"],
                        BirthDate=o_d["Patient_Information"]["BirthDate"],
                        Sex=o_d["Patient_Information"]["Sex"],
                        LastVisit_Date=last_visit_date,
                        Patient_Memo="",
                    )
                    if Patient.is_patient(Patient, p_id):
                        db.session.merge(pati)
                    else:
                        db.session.add(pati)
                    db.session.commit()

                    # Acceptance Add & Update
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
                    if Acceptance.is_acceptance(
                        selected_date=selected_date, acceptance_id=acc_id
                    ):
                        db.session.merge(acc)
                    else:
                        db.session.add(acc)
                    db.session.commit()
        return or_data

    def cancel(acceptance_id, patient_id, selected_date, acceptance_time):
        acceptance_id = acceptance_id
        acceptance_date = selected_date
        patient_id = patient_id
        acceptance_time = acceptance_time
        or_acc = ORAcceptance(selected_date=acceptance_date)
        result = or_acc.cancel(
            acc_time=acceptance_time,
            acc_id=acceptance_id,
            pati_id=patient_id,
        )
        if result["error"] == "K3":
            deleted_acc = (
                db.session.query(Acceptance)
                .filter_by(
                    Acceptance_Date=acceptance_date,
                    Acceptance_ID=acceptance_id,
                    Acceptance_Time=acceptance_time,
                    Patient_ID=patient_id,
                )
                .first()
            )
            db.session.delete(deleted_acc)
            db.session.commit()
        return result

    def get_receipt_data(data):

        result = ORAcceptance.send_receipt(data)
        return result

    def is_acceptance(acceptance_id, selected_date):
        acceptance_list = (
            db.session.query(Acceptance)
            .filter(
                Acceptance.Acceptance_ID == acceptance_id,
                Acceptance.Acceptance_Date == selected_date,
            )
            .all()
        )
        return len(acceptance_list)

    def get_list(selected_date):
        acceptance_list = (
            db.session.query(Acceptance, Patient)
            .filter(Acceptance.Acceptance_Date == selected_date)
            .filter(Acceptance.Patient_ID == Patient.Patient_ID)
            .all()
        )

        if acceptance_list is None:
            return []
        else:
            return acceptance_list

    def clear():
        pass


class AcceptanceSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Acceptance
        fields = (
            "Acceptance_ID",
            "Acceptance_Date",
            "Acceptance_Time",
            "Status",
            "Patient_ID",
            "InsuranceProvider_WholeName",
            "Department_WholeName",
            "Physician_WholeName",
            "Acceptance_Memo",
            "BigData",
        )
