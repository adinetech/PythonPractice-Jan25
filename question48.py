## Recursive Sum of List: Implement a function recursive_sum(lst) that sums all elements in a list using recursion.

def recursive_sum(list):
    if len(list) == 0:
        return 0
    else:
        return list[0] + recursive_sum(list[1:])
    
print(recursive_sum([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])) 