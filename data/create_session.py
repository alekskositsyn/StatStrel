from sqlalchemy import create_engine, text
from sqlalchemy.orm import Session
from config import settings

PATH_DB = "D:/Projects/StatStrel/database/db_statstrel.db"


def create_session() -> Session:
    engine = create_engine(f"sqlite+pysqlite:///{PATH_DB}", echo=False)
    s = Session(engine)
    return s
