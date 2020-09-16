from serve.database import db, ma


class Patient(db.Model):
    __tablename__ = "patients"
    Patient_ID = db.Column(db.String(256), primary_key=True, nullable=False)
    WholeName = db.Column(db.String(256), index=True, nullable=True)
    WholeName_inKana = db.Column(db.String(256), index=True, nullable=True)
    BirthDate = db.Column(db.String(256), nullable=True)
    Sex = db.Column(db.String(256), nullable=True)
    LastVisit_Date = db.Column(db.String(256), nullable=True)
    Patient_Memo = db.Column(db.String(256), nullable=True)

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
        Patient_Memo="",
    ):
        self.Patient_ID = Patient_ID
        self.WholeName = WholeName
        self.WholeName_inKana = WholeName_inKana
        self.BirthDate = BirthDate
        self.Sex = Sex
        self.LastVisit_Date = LastVisit_Date
        self.Patient_Memo = Patient_Memo

    def get_patient_list():
        patient_list = db.session.query(Patient).all()

        if patient_list is None:
            return []
        else:
            return patient_list

    def is_patient(self, patient_id):
        patient_list = (
            db.session.query(Patient).filter(Patient.Patient_ID == patient_id).all()
        )
        return len(patient_list)

    def regist_patient(patient):
        record = Patient(
            Patient_ID=patient["Patient_ID"],
            WholeName=patient["WholeName"],
            WholeName_inKana=patient["WholeName_inKana"],
            BirthDate=patient["BirthDate"],
            Sex=patient["Sex"],
            LastVisit_Date=patient["LastVisit_Date"],
            Patient_Memo=patient["Patient_Memo"],
        )

        db.session.add(record)
        db.session.commit()
        return patient

    def clear():
        pass


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
            "Patient_Memo",
        )
