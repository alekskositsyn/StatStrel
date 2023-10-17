from sqlalchemy import text
from sqlalchemy.orm import Session


def delete_user(s: Session, user_id):
    query = """
                DELETE FROM officers
                WHERE id = :id
                """

    s.execute(text(query), {"id": user_id})
    s.commit()
