from sqlalchemy import create_engine
from sqlalchemy.orm import Session

PATH_DB = "D:\Projects\StatStrel\database\db_statstrel.db"


def create_session() -> Session:
    engine = create_engine(f"sqlite+pysqlite:///{PATH_DB}", echo=True)
    s = Session(engine)
    return s
