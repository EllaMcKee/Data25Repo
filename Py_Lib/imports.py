from random import random
import math
from pprint import pprint

dictionary_variable = {"Danny": ["Green", "Emerald", "Turquoise"],
                       "Jade": {"FavColour": "Teal", "LeastFav": "Red"},
                       "Ensty": "Blue"}

# Get the value attached to the key of Jade, key of LeastFav.
print(dictionary_variable["Jade"]["LeastFav"])

# Get the third element of the value list.
print(dictionary_variable["Danny"][2])

# Pretty print the dictionary.
pprint(dictionary_variable)

num_float = 23.66
print(random())
print(math.ceil(num_float))
print(math.floor(num_float))
print(math.pi)
