def is_question(what):
    return what.rstrip().endswith('?')


def means_nothing(what):
    return what.strip() == ''


def hey(what):
    if what.isupper():
        return 'Whoa, chill out!'

    if is_question(what):
        return 'Sure.'

    if means_nothing(what):
        return 'Fine. Be that way!'

    return 'Whatever.'
