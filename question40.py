## Binary Search (Iterative): Write an iterative binary search function to find an element in a sorted list.

def binary_search_iterative(list, target):
    low = 0
    high = len(list) - 1
    while low <= high:
        mid = (low + high) // 2
        if list[mid] == target:
            return mid
        elif list[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return None

list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = int(input("Enter the target number: "))
print(binary_search_iterative(list, target))