from math import sqrt


def sieve(upperBound):
    """
    Searches a range of natural numbers and returns the primes values.

    :param upperBound:  indicates the upper limit of numbers to search
    :return:            the found prime values
    """

    upperBoundSquareRoot = int(sqrt(upperBound))
    # add 1 to upperBound as we're counting from 0
    isComposite = [False for i in range(1, upperBound+2)]
    for m in range(2, upperBoundSquareRoot + 1):
        if not isComposite[m]:
            for k in range(m * m, upperBound+1, m):
                isComposite[k] = True

    return [m for m in range(2, upperBound+1) if not isComposite[m]]
