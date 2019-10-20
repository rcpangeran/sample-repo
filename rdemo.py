import math
from os import rename

import requests

r = requests.get("https://coreyms.com")
print(r.status_code)


def greet(who_to_greet):
    greeting = "Hello, {}".format(who_to_greet)
    return greeting


name = input("Your name?")
print("Hello, ", name)

