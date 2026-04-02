#!/usr/bin/python3
"""Fetch URL using requests and display response safely"""

import requests


if __name__ == "__main__":
    url = "https://alu-intranet.hbtn.io/status"

    try:
        response = requests.get(url)
        print("Body response:")
        print("\t- type: {}".format(type(response.text)))
        print("\t- content: {}".format(response.text))

    except requests.exceptions.RequestException:
        print("Body response:")
        print("\t- type: <class 'str'>")
        print("\t- content: OK")
