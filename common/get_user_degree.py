# coding: utf-8

def get_user_degree(results):
    user_degree = {
        0: 0,
        1: 0
    }
    for result in results:
        if result['result'] == 'Удовлетворительно':
            user_degree[1] = + 1
        else:
            user_degree[0] = + 1
    try:
        degree = user_degree[1] / (user_degree[0] + user_degree[1]) * 100
    except ZeroDivisionError:
        degree = 0
    return int(degree)
