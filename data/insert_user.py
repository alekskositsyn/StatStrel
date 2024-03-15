from sqlalchemy import text
from sqlalchemy.orm import Session


def insert_user(s: Session, user):
    stmt = '''
                INSERT INTO user(first_name, middle_name, last_name, birth_date, group_id, personal_number, is_operator)
                VALUES (:first_name, :middle_name, :last_name, :birth_date, :group_id, :personal_number, :is_operator)
                '''
    s.execute(text(stmt), {
        "first_name": user.first_name,
        "middle_name": user.middle_name,
        "last_name": user.last_name,
        "birth_date": user.birth_date,
        "group_id": user.group_id,
        "personal_number": user.personal_number,
        "is_operator": user.is_operator,
    })
    s.commit()
