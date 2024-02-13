from sqlalchemy import text
from sqlalchemy.orm import Session


def select_users_by_search(session: Session, data):
    query = """
                select * from user
                where (user.first_name LIKE '%' :data '%') 
                or (user.last_name LIKE '%' :data '%')
                """
    rows = session.execute(text(query), {"data": data})
    return rows
