#!/usr/bin/python3
def multiple_returns(sentence):
    info_str = ()
    char = None
    if sentence:
        char = sentence[0]
    info_str = (len(sentence), char)
    return (info_str)
