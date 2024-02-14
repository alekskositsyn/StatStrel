from sqlalchemy import text
from sqlalchemy.orm import Session


def insert_user_results(s: Session, data):
    stmt1 = '''
                INSERT INTO result(user_id, scene_id, result_category_id, event_category, is_final)
                VALUES (:user_id, :scene_id, :result_category_id, :event_category, :is_final);                
                '''
    stmt2 = ''' SET @last_id_in_table1 = LAST_INSERT_ID(); '''
    stmt3 = '''
    INSERT INTO targetevents
    (result_id,Time,TypeEvent,Points,_preview_x,_preview_y,_preview_bg,_preview_target)
    VALUES
    (@last_id_in_table1, 4, 'Попадание по мишени: МВД ?06в',1,
     0.5042513421412543,
     0.4123415432621341,
     'meshes\\TargetModels\\Targets\\Sport\\ISSF\\Figure5.armesh',
     'Мишень 1'
    );'''
    stmt4 = '''
    INSERT INTO targetevents
    (result_id,Time,TypeEvent,Points)
    VALUES
    (@last_id_in_table1, 10.01, 'Упражнение завершено', 0);
    '''

    s.execute(text(stmt1), {
        "user_id": data["user_id"],
        "scene_id": 41,
        "result_category_id": 10,
        "event_category": "TargetEvents",
        "is_final": 1
    })
    s.execute(text(stmt2))
    s.execute(text(stmt3))
    s.execute(text(stmt3))
    s.execute(text(stmt3))
    s.execute(text(stmt3))
    s.execute(text(stmt4))

    s.commit()
