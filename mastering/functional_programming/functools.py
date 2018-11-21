"""
The 'functools' library is a collection of functions that return callable objects.
Some of these functions are used as decorators.

partial - no need to repeat all arguments every time
reduce - combining pairs into a single result(Mostly use in the recursive function)
"""

# ========================= Partial ===========================
# classic version
import collections
import functools
import heapq
import json
import operator
import random

heap = []
heapq.heappush(heap, 1)
heapq.heappush(heap, 2)
heapq.heappush(heap, 3)
heapq.heappush(heap, 4)
print(heapq.nsmallest(n=3, iterable=heap))

# functools.partial version
heap = []
push_callable = functools.partial(heapq.heappush, heap)
smallest_callable = functools.partial(heapq.nsmallest, iterable=heap)

for _ in range(10):
    push_callable(random.randint(0, 9))

print('heap: ', heap)
print('smallest: ', smallest_callable(5))

# ========================= Reduce ===========================
# reduce, curry, fold, accumulate, or aggregate


# >>> f = operator.mul
# >>> f(f(f(f(1, 2), 3), 4), 5)
reduce_result = functools.reduce(operator.mul, range(1, 6))
print('reduce: ', reduce_result)


# processing trees example
def tree():
    return collections.defaultdict(tree)


# Build the tree:
taxonomy = tree()
reptillia = taxonomy['Chordata']['Vertebrata']['Reptilia']
reptillia['Squamata']['Serpentes']['Pythonidae'] = [
    'Liasis', 'Morelia', 'Python'
]

# The actual contents of the tree
print(json.dumps(taxonomy, indent=4))

# The path we wish to get
path = 'Chordata.Vertebrata.Reptilia.Squamata.Serpentes'

# Split the path for easier access
path = path.split('.')

# Now fetch the path using reduce to recursively fetch the items
family = functools.reduce(lambda a, b: a[b], path, taxonomy)
print('family.items(): ', family.items())

# The path we wish to get
path = 'Chordata.Vertebrata.Reptilia.Squamata'.split('.')
suborder = functools.reduce(lambda a, b: a[b], path, taxonomy)
print('suborder.keys(): ', suborder.keys())

# fold_left = functools.reduce(
#     lambda x, y: function(x, y),
#     iterable,
#     initializer,
# )
#
# fold_right = functools.reduce(
#     lambda x, y: function(y, x),
#     reversed(iterable),
#     initializer,
# )
