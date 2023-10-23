def calc_mid_divisions(data):
    result = {
        0: 0,
        1: 0
    }
    division = ''

    for r in data:
        user_name = r.user
        division = r.division
        count = r.count
        time = r.time
        if count >= 2 and time <= 10:
            result[1] += 1
        else:
            result[0] += 1
    # print(f"В {division}: {result[0]} двоек и {result[1]} оценка удовлетворительно")
    percents = result[1] / (result[0] + result[1]) * 100
    # print(f"Percents {int(percents)}")
    return int(percents)
