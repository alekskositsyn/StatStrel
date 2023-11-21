from sqlalchemy import text
from sqlalchemy.orm import Session


def fetch_task_results_by_user_id(s: Session, user_id: int):
    query = """
        select n.count, n.time, n.date
        from number_4 n
        where n.user_id = :user_id
        order by date 
    """
    rows = s.execute(text(query), {'user_id': user_id})
    return rows
