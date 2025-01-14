## Binary Search (Recursive): Implement binary search recursively to find an element in a sorted list.

def binary_search_recursive(list, target, low, high):
    if low > high:
        return False
    else:
        mid = (low + high) // 2
        if list[mid] == target:
            return mid
        elif list[mid] > target:
            return binary_search_recursive(list, target, low, mid - 1)
        else:
            return binary_search_recursive(list, target, mid + 1, high)
        
list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 5

result = binary_search_recursive(list, target, 0, len(list) - 1)
if result == False:
    print("Element not found.")
else:
    print("Element found at index:", result)