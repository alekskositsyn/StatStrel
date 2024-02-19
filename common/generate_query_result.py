import datetime

from sqlalchemy import text


def gen_query_no_points(s, time):
    time = '00:00:' + str(time)
    stmt = '''
            INSERT INTO targetevents
            (result_id,Time,TypeEvent,Points,_preview_x,_preview_y,_preview_bg,_preview_target)
            VALUES
            (@last_id_in_table1, 
             :Time, 
             'Попадание по мишени: МВД ?06в',
             0,
             0.7419337034225464,
             -0.33728885650634766,
             'meshes\\TargetModels\\Targets\\Fire Training\\Courses of fire\\MVD\\N06v\\N06v.armesh',
             'МВД ?06в'
    );'''
    s.execute(text(stmt), {
        'Time': time,
    })


def gen_query_one_point(s, time):
    time = '00:00:' + str(time)
    stmt = '''
            INSERT INTO targetevents
            (result_id,Time,TypeEvent,Points,_preview_x,_preview_y,_preview_bg,_preview_target)
            VALUES
            (@last_id_in_table1, 
             :Time, 
             'Попадание по мишени: МВД ?06в',
             1,
             0.43758082389831543,
             0.6251684427261353,
             'meshes\\TargetModels\\Targets\\Fire Training\\Courses of fire\\MVD\\N06v\\N06v.armesh',
             'МВД ?06в'
    );'''
    s.execute(text(stmt), {
        'Time': time,
    })


def generate_query_result(s, points, count):
    sh_time = 2
    for i in range(count):
        if points:
            gen_query_one_point(s, sh_time)
            points -= 1
            sh_time += 0.5
            continue
        gen_query_no_points(s, sh_time)
        sh_time += 0.5
