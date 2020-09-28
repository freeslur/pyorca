import os

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

_engine = None
_session = None

_dburl = "sqlite:///" + os.path.join(
    os.path.abspath(os.path.dirname(__file__)), "../../db/demo.sqlite3"
)

Base = declarative_base()


def engine():
    global _engine
    return _engine


def session():
    global _session
    return _session


def init():
    global _engine, _session, _dburl
    if _engine is None and _session is None:
        _engine = create_engine(_dburl, encoding="utf-8", pool_recycle=3600, echo=True)
        _session = scoped_session(
            sessionmaker(
                bind=_engine, expire_on_commit=False, autoflush=True, autocommit=False
            )
        )
        Base.metadata.create_all(bind=_engine)


def dispose():
    global _engine, _session
    _session.close()
    _engine.dispose()
    _engine = None
    _session = None
    Base.metadata.drop_all(bind=_engine)
