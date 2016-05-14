from functools import reduce


def largest_product(string, width):

    if width < 0:
        raise ValueError("Width must be 0 or greater.")

    sections = [string[i:i+width] for i in range(len(string) - width + 1)]
    nums = [[nums for nums in map(int, list(section))] for section in sections]
    return max([reduce(lambda x, y: x * y, num, 1) for num in nums])


