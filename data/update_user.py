from sqlalchemy import text
from sqlalchemy.orm import Session


def update_user(s: Session, user_id, data):
    stmt = '''
                UPDATE user
                SET first_name = :first_name, 
                    middle_name = :middle_name,
                    last_name = :last_name,
                    group_id = :group_id,
                    birth_date = :birth_date,
                    identity_number = :identity_number, 
                    is_operator = :is_operator
                WHERE id = :id
                            '''
    s.execute(text(stmt), {
        "id": user_id,
        "first_name": data["first_name"],
        "middle_name": data["middle_name"],
        "last_name": data["last_name"],
        "group_id": data["group_id"],
        "birth_date": data["birth_date"],
        "identity_number": data["identity_number"],
        "is_operator": data["is_operator"]
    })
    s.commit()
