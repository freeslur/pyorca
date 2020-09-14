from orcalib.orpatient import ORPatient
from serve.database import db, ma


class Patient(db.Model):
    __tablename__ = "patients"

    Patient_ID = db.Column(db.String(256), primary_key=True, nullable=False)
    WholeName = db.Column(db.String(256), index=True, nullable=True)
    WholeName_inKana = db.Column(db.String(256), index=True, nullable=True)
    BirthDate = db.Column(db.String(256), nullable=True)
    Sex = db.Column(db.String(256), nullable=True)
    LastVisit_Date = db.Column(db.String(256), nullable=True)
    Memo = db.Column(db.String(256), nullable=True)

    def __repr__(self):
        return "<Patient %r>" % self.WholeName

    def __init__(
        self,
        Patient_ID,
        WholeName,
        WholeName_inKana,
        BirthDate,
        Sex,
        LastVisit_Date,
        Memo="",
    ):
        self.Patient_ID = Patient_ID
        self.WholeName = WholeName
        self.WholeName_inKana = WholeName_inKana
        self.BirthDate = BirthDate
        self.Sex = Sex
        self.LastVisit_Date = LastVisit_Date
        self.Memo = Memo

    def getPatientList():
        patient_list = db.session.query(Patient).all()

        if patient_list is None:
            return []
        else:
            return patient_list

    def isPatient(self, patient_id):
        patient_list = (
            db.session.query(Patient).filter(Patient.Patient_ID == patient_id).all()
        )
        return len(patient_list)

    def registPatient(patient):
        record = Patient(
            Patient_ID=patient["Patient_ID"],
            WholeName=patient["WholeName"],
            WholeName_inKana=patient["WholeName_inKana"],
            BirthDate=patient["BirthDate"],
            Sex=patient["Sex"],
            LastVisit_Date=patient["LastVisit_Date"],
            Memo=patient["Memo"],
        )

        db.session.add(record)
        db.session.commit()
        return patient

    def getNewbie():
        orp = ORPatient()

        data = orp.getNewbies(
            {"Base_StartDate": "2020-09-01", "Base_EndDate": "2020-09-14"}
        )
        return data


class PatientSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Patient
        fields = (
            "Patient_ID",
            "WholeName",
            "WholeName_inKana",
            "BirthDate",
            "Sex",
            "LastVisit_Date",
            "Memo",
        )
