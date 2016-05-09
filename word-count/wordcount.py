from collections import Counter
import re
import string


def word_count(phrase):
    phrase = string.lower(phrase.decode('utf-8'))
    phrase = re.sub(u'[\U0001f596_.,!&@$%^:\s]', ' ', phrase)
    return Counter(phrase.split())
