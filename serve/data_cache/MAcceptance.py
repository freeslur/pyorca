import config
from orcalib.or_acceptances import ORAcceptance
from serve.data_cache import Base, session
from sqlalchemy import Column, Integer, String


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

    @classmethod
    def query(cls):
        if not hasattr(cls, "_query"):
            cls._query = session.query_property()
        return cls._query


def get_or_acc_data():
    ora = ORAcceptance(acc_date=config.acc_date)
    data = ora.list_all()
    return data


def test():
    return Acceptance.__tablename__
