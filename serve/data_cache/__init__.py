import multiprocessing
import os
import threading
import time
from multiprocessing import Pool

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

# from multiprocessing.dummy import Pool as ThreadPool


# from serve.database import db


db_engine = create_engine(
    "sqlite:///"
    + os.path.join(
        os.path.abspath(os.path.dirname(__file__)), "../../db/demo_demo.sqlite3"
    )
)

Base = declarative_base()


Base.metadata.create_all(bind=db_engine)


def create_data(index):
    pass


p = Pool(multiprocessing.cpu_count())
d = p.map(create_data, range(1000))


# session_f = sessionmaker(bind=db_engine)
# pati = Patient()
# pati.Patient_ID = "0002"
# pati.WholeName = "aaaa"
# pati.WholeName_inKana = "abbbbb"
# pati.BirthDate = "2020-01-01"
# pati.Sex = "1"

# session_f.add(instance=pati)
# session_f.commit()

# Session = scoped_session(session_factory=session_f)
# session = Session()
# session.add(instance=pati)
# session.commit()


# class Patient(db.Model):
#     __tablename__ = "patients"
#     Patient_ID = db.Column(db.String(256), primary_key=True, nullable=False)
#     WholeName = db.Column(db.String(256), index=True, nullable=True)
#     WholeName_inKana = db.Column(db.String(256), index=True, nullable=True)
#     BirthDate = db.Column(db.String(256), nullable=True)
#     Sex = db.Column(db.String(256), nullable=True)
#     LastVisit_Date = db.Column(db.String(256), nullable=True)
#     Patient_Memo = db.Column(db.String(256), nullable=True)


# class Acceptance(db.Model):
#     __tablename__ = "acceptances"
#     Acceptance_ID = db.Column(db.String(256), primary_key=True, nullable=False)
#     Acceptance_Date = db.Column(db.String(256), primary_key=True, nullable=False)
#     Acceptance_Time = db.Column(db.String(256), index=True, nullable=False)
#     Status = db.Column(db.Integer, index=True, nullable=True)
#     Patient_ID = db.Column(db.String(256), nullable=True)
#     InsuranceProvider_WholeName = db.Column(db.String(256), nullable=True)
#     Department_WholeName = db.Column(db.String(256), nullable=True)
#     Physician_WholeName = db.Column(db.String(256), nullable=True)
#     Patient_Memo = db.Column(db.String(256), nullable=True)
#     Acceptance_Memo = db.Column(db.String(256), nullable=True)
#     BigData = db.Column(db.Text(), nullable=True)

# def f1(number):
#     session = Session()


# def thread_worker(number):
#     f1(number=number)


# def work_parallel(numbers, thread_number=0):
#     pool = ThreadPool(thread_number)
#     result = pool.map(thread_worker, numbers)
#     print(result)


# numbers = [1, 2, 3]
# work_parallel(numbers=numbers, thread_number=8)

# Session.remove()
