from itertools import chain

a = '''one two three four five six seven eight nine ten
    eleven twelve thirteen fourteen fifteen sixteen seventeen
    eighteen nineteen twenty thirty forty fifty sixty seventy
    eighty ninety hundred thousand million'''.split()

b = list(chain(range(1, 21), range(30, 101, 10), [1000, 1000000]))
nums = dict(zip(b, a))


def split_number(number, size=3):
    string = str(number)
    return [int(string[::-1][i:i + size][::-1]) for i in range(0, len(string), size)]


def tens(num):
    return num/10*10


def hundreds(num):
    return num/100*100


def parse_number(number, result=""):

    if number == 0:
        return result

    if 100 <= number < 1000:
        result += nums[number / 100] + " hundred"
        number -= hundreds(number)
        if number:
            result += " and "
    elif 20 < number < 100:
        result += nums[tens(number)]
        number -= tens(number)
        if number:
            result += '-'
    else:
        result += nums[number]
        number = 0

    return parse_number(number, result)


def say(number):
    number = int(number)
    if number == 0:
        return "zero"
    elif number < 0 or number >= 1e12:
        raise AttributeError

    lst = [parse_number(n) for n in split_number(number)]
    lst = dict(zip(['hundred', 'thousand', 'million', 'billion'], lst))

    output = ""

    if 'billion' in lst and lst['billion']:
        output = lst['billion'] + " billion"
    if 'million' in lst and lst['million']:
        if output:
            output += " " + lst['million'] + " million"
        else:
            output = lst['million'] + " million"
    if 'thousand' in lst and lst['thousand']:
        if output:
            output += " " + lst['thousand'] + " thousand"
        else:
            output = lst['thousand'] + " thousand"
    if lst['hundred']:
        if output:
            output += " "
            if 'hundred' not in lst['hundred']:
                output += "and "
        output += lst['hundred']

    return output

