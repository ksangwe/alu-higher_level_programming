#!/usr/bin/python3
"""Fetches URL using requests and displays status"""

import requests


if __name__ == "__main__":
    url = "https://alu-intranet.hbtn.io/status"

    response = requests.get(url)
    content = response.text

    print("Body response:")
    print("\t- type: {}".format(type(content)))
    print("\t- content: {}".format(content))
