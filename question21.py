## Minimum & Maximum in List: Find the minimum and maximum values in a list without using built-in min() or max().

def min_max(list):
    min = list[0]
    max = list[0]
    for i in list:
        if i < min:
            min = i
        if i > max:
            max = i
    return min, max

list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(min_max(list))