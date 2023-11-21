from sqlalchemy import text
from sqlalchemy.orm import Session


def fetch_all_tasks(s: Session):
    query = """SELECT * FROM task"""
    rows = s.execute(text(query))
    return rows
