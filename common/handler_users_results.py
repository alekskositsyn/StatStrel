def set_result(points, time, count_s):
    if points >= 3 and time < 10.02 and count_s == 4:
        return 'Удовлетворительно'
    else:
        return 'Неудовлетворительно'


def handler_users_results(rows) -> list[dict]:
    """ Обработчик данных полученных из БД,
    который подсчитывает кол-во попаданий """

    results = []
    points = 0
    count_s = 0
    flag = True
    date = ''
    time = ''
    for row in rows:
        p_target = row._preview_target
        time = row.Time.total_seconds()
        if p_target is not None and time <= 10:
            count_s += 1
            points += row.Points
            date = row.created
            time = row.Time
        elif p_target is None:
            result = set_result(points, time, count_s)
            data = {
                "date": date,
                "time": time,
                "count": count_s,
                "points": points,
                "result": result
            }
            results.append(data)

            points = 0
            count_s = 0
    return results
