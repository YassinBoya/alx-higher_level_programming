#!/usr/bin/python3

import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    res = requests.get(url, data={'email' : email})
    print(res.text)
