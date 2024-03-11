# coding: utf-8

from common.handler_users_results import handler_users_results
from data.select_results_by_user_id import select_results_by_user_id
from data.select_users_from_division import select_users_from_division


def get_division_degree(s, division_id):
    results = {
        0: 0,
        1: 0
    }
    users_rows = select_users_from_division(s, division_id)
    for user in users_rows:
        user_results = select_results_by_user_id(s, user.id)
        dict_results = handler_users_results(user_results)
        for result in dict_results:
            if result['result'] == 'Удовлетворительно':
                results[1] += 1
            else:
                results[0] += 1
    try:
        percents = results[1] / (results[0] + results[1]) * 100
    except ZeroDivisionError:
        percents = 0
    return int(percents)
