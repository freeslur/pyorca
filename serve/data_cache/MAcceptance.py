from sqlalchemy import Column, Integer, String

import config

from . import Base


class Acceptance(Base):
    __tablename__ = "acceptances"
    Acceptance_ID = Column(String(length=255), primary_key=True)
    Acceptance_Date = Column(String(length=255), primary_key=True)
    Acceptance_Time = Column(String(length=255))
    Status = Column(Integer)
    Patient_ID = Column(String(length=255))
    InsuranceProvider_WholeName = Column(String(length=255))
    Department_WholeName = Column(String(length=255))
    Physician_WholeName = Column(String(length=255))
    Acceptance_Memo = Column(String(length=255))

    def __repr__(self):
        return "<Acceptance %r>" % (self.Acceptance_ID)

    def __init__(
        self,
        acc_id,
        acc_date,
        acc_time,
        pati_id,
        status=0,
        acc_insure="",
        acc_depart="",
        acc_physic="",
        acc_memo="",
    ):
        self.Acceptance_ID = acc_id
        self.Acceptance_Date = acc_date
        self.Acceptance_Time = acc_time
        self.Status = status
        self.Patient_ID = pati_id
        self.InsuranceProvider_WholeName = acc_insure
        self.Department_WholeName = acc_depart
        self.Physician_WholeName = acc_physic
        self.Acceptance_Memo = acc_memo

    @staticmethod
    def create_dict(
        acc_id,
        acc_date,
        acc_time,
        pati_id,
        status=0,
        acc_insure="",
        acc_depart="",
        acc_physic="",
        acc_memo="",
    ):
        return {
            "Acceptance_ID": acc_id,
            "Acceptance_Date": acc_date,
            "Acceptance_Time": acc_time,
            "Status": status,
            "Patient_ID": pati_id,
            "InsuranceProvider_WholeName": acc_insure,
            "Department_WholeName": acc_depart,
            "Physician_WholeName": acc_physic,
            "Acceptance_Memo": acc_memo,
        }


def get_or_acc_data():
    acc_date = config.acc_date
