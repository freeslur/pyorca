from serve.data_cache import database
from serve.data_cache.model.models import Acceptance
from sqlalchemy import asc, bindparam, select


def get_acc(r):
    return {
        "Acceptance_Date": r[0],
        "Acceptance_ID": r[1],
        "Acceptance_Time": r[2],
        "Status": r[3],
        "Patient_ID": r[4],
    }


def select_acceptance(acc_date):
    tab = Acceptance.__table__.c
    sel = (
        select(
            [
                tab.Acceptance_Date,
                tab.Acceptance_ID,
                tab.Acceptance_Time,
                tab.Status,
                tab.Patient_ID,
            ]
        )
        .select_from(Acceptance.__table__)
        .where(tab.Acceptance_Date == acc_date)
        .order_by(asc(tab.Acceptance_ID))
    )
    accs = [get_acc(r) for r in database.session().execute(sel)]
    return accs


def insert_acceptance(data):
    database.session().execute(Acceptance.__table__.insert(), data)
    database.session().commit()


def update_acceptance(data):
    database.session().execute(
        Acceptance.__table__.update()
        .where(Acceptance.__table__.c.Acceptance_Date == bindparam("Acceptance_Date"))
        .where(Acceptance.__table__.c.Acceptance_ID == bindparam("Acceptance_ID"))
        .values(
            {
                "Acceptance_Date": bindparam("Acceptance_Date"),
                "Acceptance_ID": bindparam("Acceptance_ID"),
                "Acceptance_Time": bindparam("Acceptance_Time"),
                "Status": bindparam("Status"),
                "Patient_ID": bindparam("Patient_ID"),
            }
        ),
        data,
    )
    database.session().commit()


def delete_acceptance(data):
    database.session().execute(
        Acceptance.__table__.delete()
        .where(Acceptance.__table__.c.Acceptance_Date == bindparam("Acceptance_Date"))
        .where(Acceptance.__table__.c.Acceptance_ID == bindparam("Acceptance_ID")),
        data,
    )
    database.session().commit()
