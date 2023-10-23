from sqlalchemy import text
from sqlalchemy.orm import Session
from data.create_session import create_session


def fetch_users(session: Session, division_id, degree_id):
    query = """
                SELECT * FROM officers 
                WHERE (:did = 0 or division = :did)  
                AND (:d = 0 or degree = :d)
                """
    rows = session.execute(text(query), {"did": division_id, "d": degree_id})
    return rows


if __name__ == '__main__':
    with create_session() as s:
        data = fetch_users(s, 0, 0)
        print(list(data))
