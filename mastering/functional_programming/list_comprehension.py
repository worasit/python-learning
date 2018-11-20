"""
The list comprehension is the very easy way to apply function
or filter to a list of items. But very unreadable!
"""

import pprint
import random

pprint.pprint(f'squares: {[item ** 2 for item in range(100)]}')
pprint.pprint(f'squares with filter: {[item ** 2 for item in range(100) if item % 2==0]}')


def classic_square_filter():
    items_ = []
    for item in range(100):
        if item % 2 == 0:
            items_.append(item ** 2)
    return items_


pprint.pprint(f'classic square filter: {classic_square_filter()}')
pprint.pprint(f'random with filter: '
              f'{[random.random() for _ in range(10) if random.random() >= 0.5]}')
