from itertools import chain

a = '''one two three four five six seven eight nine ten
    eleven twelve thirteen fourteen fifteen sixteen seventeen
    eighteen nineteen twenty thirty forty fifty sixty seventy
    eighty ninety hundred thousand million'''.split()

b = list(chain(range(1, 21), range(30, 101, 10), [1000, 1000000]))
nums = dict(zip(b, a))


def split_number(number, size=3):
    """
    Split number into 3-digit chunks

    :param number:      number to split
    :param size:        chunk size
    :return:            list of chunks (billions, millions etc.)
    """

    string = str(number)
    return [int(string[::-1][i:i + size][::-1]) for i in range(0, len(string), size)]


def tens(num):
    return num/10*10


def hundreds(num):
    return num/100*100


def parse_number(number, acc=""):
    """
    Convert a number in the range 1,999 into text

    :param number:      number to convert
    :param acc:         accumulator, used for recursion
    :return:            textual number
    """

    if number == 0:
        return acc

    if 100 <= number < 1000:
        acc += nums[number / 100] + " hundred"
        number -= hundreds(number)
        if number:
            acc += " and "
    elif 20 < number < 100:
        acc += nums[tens(number)]
        number -= tens(number)
        if number:
            acc += '-'
    else:
        acc += nums[number]
        number = 0

    return parse_number(number, acc)


def build_number(lst):
    """
    Constructs a number string from the dictionary of parts

    :param lst:     dictionary containing billions, millions etc.
    :return:        full number string
    """

    output = ""
    if 'billion' in lst:
        output = lst['billion'] + " billion"
    if 'million' in lst and lst['million']:
        if output:
            output += " "
        output += lst['million'] + " million"
    if 'thousand' in lst and lst['thousand']:
        if output:
            output += " "
        output += lst['thousand'] + " thousand"
    if lst['hundred']:
        if output:
            output += " "
            if 'hundred' not in lst['hundred']:
                output += "and "
        output += lst['hundred']
    return output


def say(number):
    """
    Converts a number in range 1, 1e12-1 to text

    :param number:          number to convert
    :return:                number as text
    """

    number = int(number)
    if number == 0:
        return "zero"
    elif number < 0 or number >= 1e12:
        raise AttributeError

    lst = [parse_number(n) for n in split_number(number)]
    lst = dict(zip(['hundred', 'thousand', 'million', 'billion'], lst))

    return build_number(lst)



