
edge_cases = {'squ': 3, 'qu': 2, 'yt': 0, 'xr': 0}


def is_vowel(ch):
    return ch in "aeiou"


def contains_vowel(word):
    """
    Checks if the string parameter contains a vowel
    e.g. bacon -> 1 which is also True
    """
    for index in range(len(word)):
        if is_vowel(word[index]):
            return index
    return 0


def translate(sentence):
    """
    Translate a sentence into Pig Latin
    e.g. Anslatetray aay entencesay intoay Igpay Atinlay
    """
    result = []
    words = sentence.split(' ')
    for word in words:
        pos = contains_vowel(word)
        # check edge cases
        for prefix, value in edge_cases.items():
            if word.startswith(prefix):
                pos = value
        head, tail = word[0:pos], word[pos:]
        result.append(tail + head + "ay")

    return ' '.join(result)



print(translate("translate a sentence into pig latin"))