## Sum of List (Recursive): Write a recursive function that computes the sum of all elements in a list.

def recursive_sum(list):
    if len(list) == 0:
        return 0
    else:
        return list[0] + recursive_sum(list[1:])
    
print(recursive_sum([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))  # 55
print(recursive_sum([1, 2, 3, 4, 5]))  # 15
