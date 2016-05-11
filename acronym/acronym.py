from itertools import starmap
from re import findall


def abbreviate(title):
    words = findall(r"(\b\w)|(?:[a-z])([A-Z])\B", title)
    return ''.join(list(starmap(lambda x, y: x+y, words))).upper()
