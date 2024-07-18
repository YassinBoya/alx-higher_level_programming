#!/usr/bin/python3
""" Script that takes in a URL and an email, sends a POST request
 and displays the body of the response
"""

import sys
import urllib.request
import urllib.parse

if __name__ == "__main__":
    url = sys.argv[1]
    data = {'email': sys.argv[2]}

    data = urllib.parse.urlencode(data).encode('utf-8')

    request = urllib.request.Request(url, data)

    with urllib.request.urlopen(request) as response:
        response_data = response.read()
        print(response_data.decode('utf-8'))
