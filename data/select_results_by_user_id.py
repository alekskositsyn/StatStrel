from sqlalchemy import text
from sqlalchemy.orm import Session


def select_results_by_user_id(session: Session, user_id: int):
    query = '''
        SELECT r.id, r.created, t.Points, t.Time, t._preview_target
          FROM result r
          INNER JOIN targetevents t ON r.id = t.result_id
          where r.user_id = :user_id and r.scene_id=41
          order by r.created
    '''
    rows = session.execute(text(query), {'user_id': user_id})
    return rows
