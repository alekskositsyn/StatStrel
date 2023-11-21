from sqlalchemy import text
from sqlalchemy.orm import Session


def insert_user(s: Session, data):
    query = '''
                INSERT INTO officers(user, birthday, division, degree)
                VALUES (:user, :birthday, :division, :degree)
                '''
    s.execute(text(query), {
        "user": data["name"],
        "birthday": data["birthday"],
        "division": data["division"],
        "degree": data["degree"]
    })
    s.commit()
