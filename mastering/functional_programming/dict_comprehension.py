"""
The dict comprehension is the very easy way to apply function
or filter to a list of items as dict(key,value). But very unreadable!
"""
import pprint

squared_dict = {x: x ** 2 for x in range(10)}
squared_dict_filter = {x: x ** 2 for x in range(10) if x % 2 == 0}
pprint.pprint(f'squared_dict {type(squared_dict)}: {squared_dict}')
pprint.pprint(f'squared_dict_filter {type(squared_dict_filter)}: {squared_dict_filter}')
