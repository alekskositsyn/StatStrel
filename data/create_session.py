from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker

from common.config_load import load_config
from config import settings

PATH_DB = "D:/Projects/StatStrel/database/db_statstrel.db"


def create_session() -> Session:
    engine = create_engine(f"sqlite+pysqlite:///{PATH_DB}", echo=False)
    s = Session(engine)
    return s


def create_session_db() -> Session:
    engine = create_engine(settings.DATABASE_URL, echo=True)
    s = Session(engine)
    return s


def create_session_to_mysql(config) -> Session:
    engine = create_engine(
        f"mysql+mysqlconnector://{config['SETTINGS']['database_user']}:"
        f"{config['SETTINGS']['database_pass']}@{config['SETTINGS']['address']}:"
        f"{config['SETTINGS']['default_port']}/{config['SETTINGS']['database_name']}",
        echo=True, echo_pool=True)
    s = Session(engine)
    return s


def test_session_mysql(config) -> bool:
    engine = create_engine(
        f"mysql+mysqlconnector://{config['database_user']}:"
        f"{config['database_pass']}@{config['address']}:"
        f"{config['default_port']}/{config['database_name']}",
        echo=True, echo_pool=True)
    try:
        engine.connect()
        s = Session(engine)
        s.close()
        return True
    except Exception as e:
        print(e)
        return False
