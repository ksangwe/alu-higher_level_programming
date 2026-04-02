#!/usr/bin/python3
"""Gets X-Request-Id from response header"""

import sys
import urllib.request


if __name__ == "__main__":
    url = sys.argv[1]

    with urllib.request.urlopen(url) as response:
        headers = response.headers
        print(headers.get("X-Request-Id"))
