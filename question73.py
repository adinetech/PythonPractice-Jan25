## Flatten Nested List (Recursive): Write a recursive function that takes a list which may contain nested lists and returns a flat list of all elements.

def flatten_list(lst):
    flat_list = []
    for i in lst:
        if type(i) == list:
            flat_list.extend(flatten_list(i))
        else:
            flat_list.append(i)
    return flat_list

print(flatten_list([1, 2, 3, [4, 5], 6, [7, 8, 9]]))