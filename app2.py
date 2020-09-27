import os

from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base

db_engine = create_engine(
    "sqlite:///"
    + os.path.join(os.path.abspath(os.path.dirname(__file__)), "db/demo222.sqlite3")
)

Base = declarative_base()


Base.metadata.create_all(bind=db_engine)


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


class Acceptance(Base):
    __tablename__ = "acceptances"
    Acceptance_ID = Column(String(length=255), primary_key=True)
    Acceptance_Date = Column(String(length=255), primary_key=True)
    Acceptance_Time = Column(String(length=255))
    Status = Column(Integer)
    Patient_ID = Column(String(length=255))
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
        acc_memo="",
    ):
        self.Acceptance_ID = acc_id
        self.Acceptance_Date = acc_date
        self.Acceptance_Time = acc_time
        self.Status = status
        self.Patient_ID = pati_id
        self.Acceptance_Memo = acc_memo

    @staticmethod
    def create_dict(
        acc_id,
        acc_date,
        acc_time,
        pati_id,
        status=0,
        acc_memo="",
    ):
        return {
            "Acceptance_ID": acc_id,
            "Acceptance_Date": acc_date,
            "Acceptance_Time": acc_time,
            "Status": status,
            "Patient_ID": pati_id,
            "Acceptance_Memo": acc_memo,
        }
