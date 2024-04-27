#!/usr/bin/python3
"""sends a request to the URL and displays the value of the
X-Request-Id variable found in the header of the response."""

if __name__ == '__main__':
    import sys
    import urllib.request

    if len(sys.argv) != 2:
        print("Usage: python script.py <URL>")
        sys.exit(1)

    url = sys.argv[1]

    try:
        with urllib.request.urlopen(url) as r:
            request_id = r.getheader('X-Request-Id')
            if request_id:
                print(request_id)
            else:
                print("X-Request-Id header not found in the response.")
    except Exception as e:
        print("An error occurred:", e)
