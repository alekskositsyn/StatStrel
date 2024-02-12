from pprint import pprint

from sqlalchemy import create_engine, text
from sqlalchemy.orm import Session
from config import settings
from data.select_results_by_user_id import select_results_by_user_id


def create_session_with_mysql() -> Session:
    engine = create_engine(settings.DATABASE_URL, echo=True)
    s = Session(engine)
    return s


data = {}
# create_session_with_mysql = create_engine(url=settings.DATABASE_URL, echo=True)
with create_session_with_mysql() as s:
    points = 0
    count_s = 0
    flag = True
    date = ''
    time = ''

    rows = select_results_by_user_id(s, 2)
    for row in rows:
        p_target = row._preview_target
        time = row.Time.total_seconds()
        if p_target is not None and time <= 10:
            count_s += 1
            points += row.Points
            date = row.created
            time = row.Time
        elif p_target is None:
            data[row.id] = {
                "date": date,
                "time": time,
                "count": count_s,
                "points": points,
            }
            points = 0
            count_s = 0

    print(data)



    # pprint(rows.all())
