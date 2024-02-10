from sqlalchemy import text
from sqlalchemy.orm import Session


def insert_user(s: Session, data):
    stmt = '''
                INSERT INTO user(first_name, middle_name, last_name, birth_date, group_id, identity_number, is_operator)
                VALUES (:first_name, :middle_name, :last_name, :birth_date, :group_id, :identity_number, :is_operator)
                '''
    s.execute(text(stmt), {
        "first_name": data["first_name"],
        "middle_name": data["middle_name"],
        "last_name": data["last_name"],
        "birth_date": data["birth_date"],
        "group_id": data["group_id"],
        "identity_number": data["identity_number"],  # TODO обработать событие нажатия
        "is_operator": data["is_operator"],
    })
    s.commit()
