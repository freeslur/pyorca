from sqlalchemy import Column, String

from . import Base


class Patient(Base):
    __tablename__ = "patients"
    Patient_ID = Column(String(length=255), primary_key=True)
    WholeName = Column(String(length=255))
    WholeName_inKana = Column(String(length=255))
    BirthDate = Column(String(length=255))
    Sex = Column(String(length=255))
    LastVisit_Date = Column(String(length=255))
    Patient_Memo = Column(String(length=255))

    def __repr__(self):
        return "<Patient %r>" % (self.Patient_ID)

    def __init__(
        self,
        pati_id,
        pati_name,
        pati_kana,
        pati_birth,
        pati_sex,
        pati_lastvisit="",
        pati_memo="",
    ):
        self.Patient_ID = pati_id
        self.WholeName = pati_name
        self.WholeName_inKana = pati_kana
        self.BirthDate = pati_birth
        self.Sex = pati_sex
        self.LastVisit_Date = pati_lastvisit
        self.Patient_Memo = pati_memo

    @staticmethod
    def create_dict(
        pati_id,
        pati_name,
        pati_kana,
        pati_birth,
        pati_sex,
        pati_lastvisit="",
        pati_memo="",
    ):
        return {
            "Patient_ID": pati_id,
            "WholeName": pati_name,
            "WholeName_inKana": pati_kana,
            "BirthDate": pati_birth,
            "Sex": pati_sex,
            "LastVisit_Date": pati_lastvisit,
            "Patient_Memo": pati_memo,
        }
