from pprint import pprint

from orcalib.or_acceptances import ORAcceptance
from serve.data_cache import database
from serve.data_cache.caching import (
    delete_acceptance,
    insert_acceptance,
    select_acceptance,
    update_acceptance,
)
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
database.init()
accdiff = AccDiff()

prev = select_acceptance(acc_date="2020-09-25")
accdiff.diff(prev, acc_data)
if len(accdiff.added()):
    insert_acceptance(accdiff.added())
if len(accdiff.changed()):
    update_acceptance(accdiff.changed())
if len(accdiff.removed()):
    delete_acceptance(accdiff.removed())
pprint(
    {"add": accdiff.added(), "change": accdiff.changed(), "remove": accdiff.removed()}
)
nows = select_acceptance(acc_date="2020-09-25")
pprint(nows)
pprint(acc_data)
