from sqlalchemy import text
from sqlalchemy.orm import Session

from common.generate_query_result import generate_query_result


def insert_user_results(s: Session, user_id, points, count, time, date):
    result_query = '''
                INSERT INTO result(user_id, scene_id, result_category_id, event_category,created, is_final)
                VALUES (:user_id, :scene_id, :result_category_id, :event_category, :created, :is_final);                
                '''
    s.execute(text(result_query), {
        "user_id": user_id,
        "scene_id": 41,
        "result_category_id": 10,
        "event_category": "TargetEvents",
        "created": date,
        "is_final": 1
    })
    stmt2 = ''' SET @last_id_in_table1 = LAST_INSERT_ID(); '''
    s.execute(text(stmt2))

    generate_query_result(s, points, count)
    time = '00:00:' + str(time)
    stmt4 = '''
                INSERT INTO targetevents
                (result_id,Time,TypeEvent,Points)
                VALUES
                (@last_id_in_table1, :time, 'Упражнение завершено', 0);
    '''
    s.execute(text(stmt4), {'time': time})
    s.flush()
    s.commit()
