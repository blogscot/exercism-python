import string

alphabet = string.ascii_lowercase

def is_pangram(phrase):
    return all(alpha in phrase.lower() for alpha in alphabet)
