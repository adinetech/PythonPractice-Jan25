## Reverse List: Reverse a list in-place (without using reversed() or slicing).

def reverse_list(list):
    list.reverse()
    return list

list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(reverse_list(list))
