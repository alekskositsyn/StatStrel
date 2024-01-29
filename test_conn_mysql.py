from pprint import pprint

from sqlalchemy import create_engine, text
from sqlalchemy.orm import Session
from config import settings


def create_session_with_mysql() -> Session:
    engine = create_engine(settings.DATABASE_URL, echo=True)
    s = Session(engine)
    return s


# create_session_with_mysql = create_engine(url=settings.DATABASE_URL, echo=True)
with create_session_with_mysql() as s:
    query = """SELECT * FROM user"""
    rows = s.execute(text(query))
    pprint(rows.all())
