from sqlalchemy import text
from sqlalchemy.orm import Session


def fetch_task_4(s: Session, division_id):
    query = """
        select o.user, o.division, n.count, n.time
        from officers o
        join main.number_4 n on o.id = n.user_id
        where o.division = :division_id
    """
    rows = s.execute(text(query), {'division_id': division_id})
    return rows
