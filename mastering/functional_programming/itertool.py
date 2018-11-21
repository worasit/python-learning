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
numbers = [10, 9, 6, 3, 2, 5]
itertools.accumulate(numbers, operator.add)
