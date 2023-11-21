from sqlalchemy import text
from sqlalchemy.orm import Session


def fetch_all_divisions(s: Session):
    query = """SELECT * FROM divisions"""
    rows = s.execute(text(query))
    return rows
