#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        res = fct(args[0], args[1])
        return (res)
    except Exception as ex:
        print("Exception: {}".format(ex), file=sys.stderr)
        return (None)