from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column
from sqlalchemy.sql.sqltypes import BIGINT
from sqlalchemy.sql.sqltypes import Integer
from sqlalchemy.sql.sqltypes import String
from sqlalchemy.sql.sqltypes import DateTime
from sqlalchemy.sql.sqltypes import UnicodeText
from sqlalchemy.sql.sqltypes import Boolean


BASE = declarative_base()


def get_db_engine(conn_str, debug=False):
    engine = create_engine(conn_str, echo=debug)
    return engine


def get_db_session(conn_str, debug=False):
    sessmaker = sessionmaker(bind=get_db_engine(conn_str, debug))
    session = sessmaker()
    return session


def init_db(conn_str):
    BASE.metadata.create_all(get_db_engine(conn_str, False))
