#!/usr/bin/python3
"""A script that fetches https://alx-intranet.hbtn.io/status"""
import urllib.request as urllib

if __name__ == "__main__":
    with urllib.urlopen('https://alx-intranet.hbtn.io/status') as response:
        content = response.read()
    print("Body response:")
    print(f"\t- type: {type(content)}")
    print(f"\t- content: {content}")
    print(f"\t- utf8 content: {content.decode('UTF-8')}")
