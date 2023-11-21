from sqlalchemy import text
from sqlalchemy.orm import Session


def fetch_all_degree(s: Session):
    query = """SELECT * FROM degree"""
    rows = s.execute(text(query))
    return rows
