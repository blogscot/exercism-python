def detect_anagrams(word, items):

    return [item for item in items
            if sorted(word.lower()) == sorted(item.lower()) and
            word.lower() != item.lower()]
