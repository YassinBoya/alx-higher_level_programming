#!/usr/bin/python3
def weight_average(my_list=[]):
    total_weight = 0
    weighted_sum = 0
    if not my_list:
        return (0)
    for row in my_list:
        score, weight = row
        total_weight += weight
        weighted_sum += score * weight
    return (weighted_sum / total_weight)
