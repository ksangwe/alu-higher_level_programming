#!/usr/bin/python3
"""Fetch URL using requests and display response"""

import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]

    try:
        response = requests.get(url)
        content = response.text

        print("Body response:")
        print("\t- type: {}".format(type(content)))
        print("\t- content: {}".format(content))

    except requests.exceptions.RequestException:
        print("Body response:")
        print("\t- type: <class 'str'>")
        print("\t- content: Error")
