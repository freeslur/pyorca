import os

from sqlalchemy import MetaData, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

metadata = MetaData()
db_engine = create_engine(
    "sqlite:///"
    + os.path.join(os.path.abspath(os.path.dirname(__file__)), "../../db/demo.sqlite3"),
    encoding="utf-8",
    pool_recycle=3600,
)
session = scoped_session(
    sessionmaker(
        bind=db_engine, expire_on_commit=False, autoflush=True, autocommit=False
    )
)
Base = declarative_base()


metadata.create_all(bind=db_engine)
