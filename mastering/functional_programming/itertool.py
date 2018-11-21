"""
The itertools library contains iterable functions inspired by those
available in functional languages.

Pros
- Minimal amount of memory is required to process the largest of datasets
- Memory efficient
- Fast
- Tested


accumulate   - reduce with intermediate results
chain        - combining multiple results
combinations - combinatorics in Python
permutation  - combinations where the order matters
compress     - selecting items using a list of Booleans
dropwhile/takewhile - selecting items using a function
count        - infinite range with decimal steps
groupby      - grouping your sorted iterable
islice       - slicing any iterable
"""
import operator
import itertools

# accumulate
import pprint
import time

numbers = [10, 9, 6, 3, 2, 5]
print(list(itertools.accumulate(numbers, operator.add)))

# chain
list_a = [1, 2, 3]
list_b = [4, 5, 6]
print(list(itertools.chain(list_a, list_b)))

# combinations
list_a = [1, 2, 3, 4, 5, 6]
pprint.pprint(list(itertools.combinations(list_a, 2)))
list_b = [0, 1]
pprint.pprint(list(itertools.combinations_with_replacement(list_b, 2)))

# permutation (ordered is matter)
# [(0, 1), (0, 2), (1, 2)]
# [(0, 1), (0, 2), (1, 0), (1, 2), (2, 0), (2, 1)]
pprint.pprint(list(itertools.combinations(range(3), 2)))
pprint.pprint(list(itertools.permutations(range(3), 2)))

# compress - to filter the value from a large dataset using booleans
# [1, 2]
pprint.pprint(list(itertools.compress(range(5), [0, 1, 1, 0, 0])))

# dropwhile/takewhile
pprint.pprint(list(itertools.dropwhile(lambda x: x <= 5, [1, 2, 3, 4, 5, 6, 7, 8, 9])))
pprint.pprint(list(itertools.takewhile(lambda x: x <= 5, [1, 2, 3, 4, 5, 6, 7, 8, 9])))

# count

# Except for being infinite, the standard version returns the same
# results as the range function does.
pprint.pprint([(a, b) for a, b in zip(range(3), itertools.count())])
pprint.pprint([(a, b) for a, b in zip(range(3), itertools.count(0, 0.01))])

# groupby
# The input needs to be sorted by the 'group' parameter. Otherwise it will be added as a separate group
# The results are available for use only once.  So after processing a group, it will not be available anymore.
items = [('a', 1), ('a', 2), ('b', 2), ('b', 0), ('c', 3)]
for group, items in itertools.groupby(items, lambda x: x[0]):
    print('%s: %s' % (group, [v for k, v in items]))
# a: [1, 2]
# # b: [2, 0]
# # c: [3]


# islice - mostly use for limit the infinite count
print(list(itertools.islice(itertools.count(0, 0.01), 5, 10)))
