from math import sqrt
import itertools as it


def sieve(upperBound):
    """
    Searches a range of natural numbers and returns the primes values.

    Tiphat: cds-amal

    :param upperBound:  indicates the upper limit of numbers to search
    :return:            the found prime values
    """

    upperBoundSquareRoot = int(sqrt(upperBound))
    primes = [False, False] + [True] * upperBound
    for m in it.chain([2], range(3, upperBoundSquareRoot + 1)):
        if primes[m]:
            for k in range(m * m, upperBound+1, m):
                primes[k] = False

    return list(it.compress(range(upperBound+1), primes))

