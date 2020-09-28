from pprint import pprint

from serve.data_cache import database
from serve.data_cache.caching import (
    delete_acceptance,
    insert_acceptance,
    select_acceptance,
    update_acceptance,
)
from utils.diff import AccDiff

a = [
    {
        "Acceptance_Date": "2020-09-25",
        "Acceptance_ID": "00001",
        "Acceptance_Time": "13:19:52",
        "Status": 2,
        "Patient_ID": "00005",
    },
    {
        "Acceptance_Date": "2020-09-25",
        "Acceptance_ID": "00002",
        "Acceptance_Time": "13:20:11",
        "Status": 0,
        "Patient_ID": "00008",
    },
    {
        "Acceptance_Date": "2020-09-25",
        "Acceptance_ID": "00003",
        "Acceptance_Time": "13:20:22",
        "Status": 0,
        "Patient_ID": "00010",
    },
    {
        "Acceptance_Date": "2020-09-25",
        "Acceptance_ID": "00004",
        "Acceptance_Time": "17:32:52",
        "Status": 0,
        "Patient_ID": "00002",
    },
]
b = [
    {
        "Acceptance_Date": "2020-09-25",
        "Acceptance_ID": "00006",
        "Acceptance_Time": "17:42:52",
        "Status": 0,
        "Patient_ID": "00002",
    },
    {
        "Acceptance_Date": "2020-09-25",
        "Acceptance_ID": "00001",
        "Acceptance_Time": "13:19:52",
        "Status": 2,
        "Patient_ID": "00005",
    },
    {
        "Acceptance_Date": "2020-09-25",
        "Acceptance_ID": "00003",
        "Acceptance_Time": "13:20:22",
        "Status": 2,
        "Patient_ID": "00010",
    },
    {
        "Acceptance_Date": "2020-09-25",
        "Acceptance_ID": "00005",
        "Acceptance_Time": "17:42:52",
        "Status": 0,
        "Patient_ID": "00002",
    },
]

database.init()
accd = AccDiff()

prev = select_acceptance("2020-09-25")
accd.diff(prev, b)
if len(accd.added()):
    insert_acceptance(accd.added())
if len(accd.changed()):
    update_acceptance(accd.changed())
if len(accd.removed()):
    delete_acceptance(accd.removed())
pprint({"add": accd.added(), "change": accd.changed(), "remove": accd.removed()})
nows = select_acceptance("2020-09-25")
pprint(nows)
pprint(b)
