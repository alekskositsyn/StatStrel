from sqlalchemy import text
from sqlalchemy.orm import Session


def select_users_from_division(session: Session, division_id: int):
    query = '''
    select id from user where group_id = :division_id
    '''
    rows = session.execute(
        text(query), {'division_id': division_id}
    )
    return rows
