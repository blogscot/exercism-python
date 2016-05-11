def find_multiples(upper_bound, value):
    return [i for i in range(value, upper_bound, value)]


def sum_of_multiples(upper_bound, multiples):
    return sum(set(sum([find_multiples(upper_bound, value)
                        for value in multiples if value], [])))


