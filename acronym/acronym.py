from re import findall


def abbreviate(title):
    words = findall(r"[A-Z]+[a-z]*|[a-z]+", title)
    return ''.join([word[0] for word in words]).upper()
