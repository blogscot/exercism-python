from collections import Counter


def encode(seq):
    my_dict = dict(Counter(list(seq)))
    print my_dict

    values = [str(my_dict[key]) + key for key in sorted(my_dict.keys())]
    return ''.join(values)


def decode(seq):
    return ''.join([int(seq[i: i+1]) * str(seq[i+1:i+2]) for i in range(0, len(seq), 2)])
