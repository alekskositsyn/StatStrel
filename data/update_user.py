from sqlalchemy import text
from sqlalchemy.orm import Session


def update_user(s: Session, user_id, data):
    query = '''
                UPDATE officers
                SET user = :user, 
                    birthday = :birthday,
                    division = :division, 
                    degree = :degree
                WHERE id = :id
                            '''
    s.execute(text(query), {
        "id": user_id,
        "user": data["name"],
        "birthday": data["birthday"],
        "division": data["division"],
        "degree": data["degree"]
    })
    s.commit()
