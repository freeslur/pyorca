from orcalib.oracceptances import ORAcceptance
from orcalib.orpatient import ORPatient
from serve.database import db, ma
from serve.models.patient import Patient


class Acceptance(db.Model):
    __tablename__ = "acceptances"

    Acceptance_ID = db.Column(db.String(256), primary_key=True, nullable=False)
    Acceptance_Date = db.Column(db.String(256), index=True, nullable=False)
    Acceptance_Time = db.Column(db.String(256), index=True, nullable=False)
    Status = db.Column(db.Integer, index=True, nullable=True)
    Patient_ID = db.Column(db.String(256), nullable=True)
    InsuranceProvider_WholeName = db.Column(db.String(256), nullable=True)
    Department_WholeName = db.Column(db.String(256), nullable=True)
    Patient_Memo = db.Column(db.String(256), nullable=True)
    Acceptance_Memo = db.Column(db.String(256), nullable=True)

    def __repr__(self):
        return "<Acceptance %r>" % self.WholeName

    def __init__(
        self,
        Acceptance_ID,
        Acceptance_Date,
        Acceptance_Time,
        Status,
        Patient_ID,
        InsuranceProvider_WholeName,
        Department_WholeName,
        Acceptance_Memo="",
    ):
        self.Acceptance_ID = Acceptance_ID
        self.Acceptance_Date = Acceptance_Date
        self.Acceptance_Time = Acceptance_Time
        self.Status = Status
        self.Patient_ID = Patient_ID
        self.InsuranceProvider_WholeName = InsuranceProvider_WholeName
        self.Department_WholeName = Department_WholeName
        self.Acceptance_Memo = Acceptance_Memo

    def check():
        or_data = ORAcceptance.list_all()
        if or_data["error"] == "00":
            for o_d in or_data["data"]:
                p_id = o_d["Patient_Information"]["Patient_ID"]
                acc_id = o_d["Acceptance_ID"]

                # Patient Add & Update
                orp = ORPatient()
                last_visit_date = orp.get_prev_date(patient_id=p_id)
                pati = Patient(
                    Patient_ID=p_id,
                    WholeName=o_d["Patient_Information"]["WholeName"],
                    WholeName_inKana=o_d["Patient_Information"]["WholeName_inKana"],
                    BirthDate=o_d["Patient_Information"]["BirthDate"],
                    Sex=o_d["Patient_Information"]["Sex"],
                    LastVisit_Date=last_visit_date,
                )
                if Patient.isPatient(Patient, p_id):
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
                )
                if Acceptance.isAcceptance(Acceptance, acc_id):
                    db.session.merge(acc)
                else:
                    db.session.add(acc)
                db.session.commit()
        return or_data

    def isAcceptance(self, acceptance_id):
        acceptance_list = (
            db.session.query(Acceptance)
            .filter(
                Acceptance.Acceptance_ID == acceptance_id,
                Acceptance.Acceptance_Date == "2020-09-14",
            )
            .all()
        )
        return len(acceptance_list)

    def getList():
        acceptance_list = db.session.query(Acceptance).all()

        if acceptance_list is None:
            return []
        else:
            return acceptance_list

    def regist(acceptance):

        record = Acceptance(
            Acceptance_ID=acceptance["Acceptance_ID"],
            Acceptance_Date=acceptance["Acceptance_Date"],
            Acceptance_Time=acceptance["Acceptance_Time"],
            Status=acceptance["Status"],
            Patient_ID=acceptance["Patient_ID"],
            InsuranceProvider_WholeName=acceptance["InsuranceProvider_WholeName"],
            Department_WholeName=acceptance["Department_WholeName"],
            Acceptance_Memo=acceptance["Acceptance_Memo"],
        )

        db.session.add(record)
        db.session.commit()
        return acceptance


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
            "Acceptance_Memo",
        )
