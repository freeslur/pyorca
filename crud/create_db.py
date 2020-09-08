import sqlite3

conn = sqlite3.connect("kartedb.sqlite3")

c = conn.cursor()

c.execute(
    """CREATE TABLE patients
(Patient_ID TEXT PRIMARY KEY,
WholeName TEXT,
WholeName_inKana TEXT,
BirthDate TEXT,
Sex TEXT)"""
)

conn.commit()
c.execute(
    """CREATE TABLE acceptances
(ID INTEGER PRIMARY KEY AUTOINCREMENT,
Acceptance_ID TEXT,
Patient_ID TEXT,
WholeName TEXT,
WholeName_inKana TEXT,
BirthDate TEXT,
Status TEXT,
Acceptance_Date TEXT,
Acceptance_Time TEXT,
InsuranceProvider_WholeName TEXT,
Department_WholeName TEXT,
Physician_WholeName TEXT,
Previouse_Acceptance_Date TEXT,
Patient_Memo TEXT,
Acceptance_Memo TEXT)"""
)

conn.commit()
c.execute("SELECT * FROM patients")
result = c.fetchall()
print(result)
conn.close()
