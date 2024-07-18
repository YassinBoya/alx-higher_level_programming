#!/usr/bin/python3
"""
Python Script that takes in a URL, sends a request to the URL
& displays the body of the response
"""

import requests
import sys

if __name__ == '__main__':
    url = sys.argv[1]
    try:
        res = requests.get(url)
        print(res.text)
    except error.HTTPError as er:
        print('Error code:', er.error)
