def calc_mid_divisions(data):
    result = {
        0: 0,
        1: 0
    }
    users_id = []
    division = ''

    for r in data:
        user_id = r.id
        division = r.division
        count = r.count
        time = r.time
        if user_id in users_id:
            continue
        if count >= 2 and time <= 10:
            result[1] += 1
            users_id.append(user_id)
        else:
            result[0] += 1
            users_id.append(user_id)

    print(f"В {division}: {result[0]} двоек и {result[1]} оценка удовлетворительно")
    percents = result[1] / (result[0] + result[1]) * 100
    print(users_id)
    return int(percents)
