from math import sqrt, ceil
from itertools import chain


def prime_factors(num):
    if num == 1:
        return []
    # loop factor values in range 2, sqrt(num)
    upper_bound = int(ceil(sqrt(num)))
    for n in range(2, upper_bound + 1):
        # if value is factor save and repeat
        if num % n == 0:
            return list(chain([n], prime_factors(num // n)))

    return [num]
