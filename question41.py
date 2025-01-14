## Remove Duplicates from List: Given a list with duplicates, create a new list with unique elements only.

def remove_duplicates(list):
    return list(set(list))

list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5]
print(remove_duplicates(list))