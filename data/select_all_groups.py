from sqlalchemy import text
from sqlalchemy.orm import Session


def select_all_groups(s: Session):
    query = """SELECT * FROM `group`"""
    rows = s.execute(text(query))
    return rows
