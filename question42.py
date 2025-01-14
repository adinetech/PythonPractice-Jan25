## Second Largest Element: Find the second largest element in a list of unique integers.

def second_largest(list):
    list.sort()
    return list[-2]

list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11,]
list.sort()
print(second_largest(list))