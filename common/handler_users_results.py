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
            data = {
                "date": date,
                "time": time,
                "count": count_s,
                "points": points,
            }
            results.append(data)

            points = 0
            count_s = 0
    return results
