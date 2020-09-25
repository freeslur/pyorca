import os

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

db_engine = create_engine(
    "sqlite:///"
    + os.path.join(os.path.abspath(os.path.dirname(__file__)), "../../db/demo.sqlite3")
)

Base = declarative_base()


Base.metadata.create_all(bind=db_engine)
