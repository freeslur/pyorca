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
c.execute("SELECT * FROM patients")
result = c.fetchall()
print(result)
conn.close()
