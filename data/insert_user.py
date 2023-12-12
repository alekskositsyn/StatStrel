from sqlalchemy import text
from sqlalchemy.orm import Session


def insert_user(s: Session, data):
    stmt = '''
                INSERT INTO officers(user, birthday, division, degree)
                VALUES (:user, :birthday, :division, :degree)
                '''
    s.execute(text(stmt), {
        "user": data["name"],
        "birthday": data["birthday"],
        "division": data["division"],
        "degree": data["degree"]
    })
    s.commit()
