from serve.data_cache import Base
from sqlalchemy import Column, String


class Patient(Base):
    __tablename__ = "patients"
    Patient_ID = Column(String(length=255), primary_key=True)
    Patient_Memo = Column(String(length=255))

    def __repr__(self):
        return "<Patient %r>" % (self.Patient_ID)

    def __init__(
        self,
        pati_id,
        pati_memo="",
    ):
        self.Patient_ID = pati_id
        self.Patient_Memo = pati_memo

    @staticmethod
    def create_dict(
        pati_id,
        pati_memo="",
    ):
        return {
            "Patient_ID": pati_id,
            "Patient_Memo": pati_memo,
        }
