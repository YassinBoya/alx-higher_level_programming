#!/usr/bin/python3
"""
Python script that takes in a URL, sends a request to the URL 
and displays the body of the response (decoded in utf-8).
"""


if __name__ == "__main__":
    import sys
    from urllib import request, error
    url = sys.argv[1]

    req = request.Request(url)
    try:
        with request.urlopen(req) as res:
            print(res.read().decode('utf-8'))
    except error.HTTPError as er:
        print('Error code:', er.code)
