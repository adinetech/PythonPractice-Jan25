## Invert Dictionary: Given a dictionary, invert it (keys become values, values become keys).

original= {'a': 1, 'b': 2, 'c': 3}
inverted = {v: k for k, v in original.items()}
print(inverted)