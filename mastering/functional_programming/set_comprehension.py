"""
The set comprehension is similar to list comprehension, but return the set(hashable type)
"""
import pprint

squares = {item ** 2 for item in range(10)}
squared_filter = {item ** 2 for item in range(10) if item % 2 == 0}

pprint.pprint(f'squares {type(squares)}: {squares}')
pprint.pprint(f'square_filter {type(squared_filter)}: {squared_filter}')
