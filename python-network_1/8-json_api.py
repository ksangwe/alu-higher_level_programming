#!/usr/bin/python3
"""Search user API and handle JSON response"""

import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) > 1:
        q = sys.argv[1]
    else:
        q = ""

    data = {"q": q}

    response = requests.post("http://0.0.0.0:5000/search_user", data=data)

    try:
        result = response.json()

        if result == {}:
            print("No result")
        else:
            print("[{}] {}".format(result.get("id"), result.get("name")))

    except ValueError:
        print("Not a valid JSON")
