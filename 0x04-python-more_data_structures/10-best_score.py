#!/usr/bin/python3
def best_score(a_dictionary):
    HKey_value = 0
    Best_key = None
    if a_dictionary:
        for key, value in a_dictionary.items():
            if value > HKey_value:
                Best_key = key
                HKey_value = value
        return Best_key
