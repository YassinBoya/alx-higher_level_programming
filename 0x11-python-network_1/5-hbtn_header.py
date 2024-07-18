#!/usr/bin/python3


import requests, sys


if __name__ == "__main__":
    url = sys.argv[1]
    req = requests.get(url)
    data = req.headers.get("X-Request-Id")
    print(data)
