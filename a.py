from pprint import pprint

from sqlalchemy import and_, desc, func, insert, select, update

from orcalib.or_acceptances import ORAcceptance
from serve import data_cache
from serve.data_cache.MAcceptance import Acceptance, test
from utils.diff import AccDiff

ora = ORAcceptance(acc_date="2020-09-25")
data = ora.list_all()
acc_data = []
pati_data = []
for d in data["data"]:
    acc_d = {
        "Acceptance_Date": d["Acceptance_Date"],
        "Acceptance_ID": d["Acceptance_ID"],
        "Acceptance_Time": d["Acceptance_Time"],
        "Status": int(d["Status"]),
        "Patient_ID": d["Patient_Information"]["Patient_ID"],
    }
    acc_data.append(acc_d)
    pati_data.append({"Patient_ID": d["Patient_Information"]["Patient_ID"]})

pprint(acc_data)
# print(acc_data)
data_cache
accs = Acceptance.query().order_by(desc(Acceptance.Acceptance_ID)).all()
pprint(accs)

a = [
    {
        "Acceptance_Date": "2020-09-25",
        "Acceptance_ID": "00001",
        "Acceptance_Time": "13:19:52",
        "Status": "2",
        "Patient_ID": "00005",
    },
    {
        "Acceptance_Date": "2020-09-25",
        "Acceptance_ID": "00002",
        "Acceptance_Time": "13:20:11",
        "Status": "0",
        "Patient_ID": "00008",
    },
    {
        "Acceptance_Date": "2020-09-25",
        "Acceptance_ID": "00003",
        "Acceptance_Time": "13:20:22",
        "Status": "0",
        "Patient_ID": "00010",
    },
    {
        "Acceptance_Date": "2020-09-25",
        "Acceptance_ID": "00004",
        "Acceptance_Time": "17:32:52",
        "Status": "0",
        "Patient_ID": "00002",
    },
]
b = [
    {
        "Acceptance_Date": "2020-09-25",
        "Acceptance_ID": "00001",
        "Acceptance_Time": "13:19:52",
        "Status": "2",
        "Patient_ID": "00005",
    },
    {
        "Acceptance_Date": "2020-09-25",
        "Acceptance_ID": "00003",
        "Acceptance_Time": "13:20:22",
        "Status": "0",
        "Patient_ID": "00010",
    },
    {
        "Acceptance_Date": "2020-09-25",
        "Acceptance_ID": "00004",
        "Acceptance_Time": "17:32:52",
        "Status": "2",
        "Patient_ID": "00002",
    },
    {
        "Acceptance_Date": "2020-09-25",
        "Acceptance_ID": "00005",
        "Acceptance_Time": "17:42:52",
        "Status": "0",
        "Patient_ID": "00002",
    },
]
