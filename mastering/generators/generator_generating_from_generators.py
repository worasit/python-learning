import itertools


# Powerset
def powerset(sequence):
    for size in range(len(sequence) + 1):
        yield from itertools.combinations(sequence, size)


for result in powerset('abc'):
    print(result)


# Flatten
def flatten(sequence):
    """
    This code uses `TypeError` to detect non-iterable objects.
    The result is that if the sequence(which could be a generator) returns
    a `TypeError`, it will silently hide it.
    :param sequence:
    """
    for item in sequence:
        try:
            yield from flatten(item)
        except TypeError:
            yield item


print(list(flatten([1, [2, [3, [4, 5], 6], 7], 8, (9, 10, 11)])))
