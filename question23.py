## Count Occurrences in List: Given a list of integers, prompt for a specific integer and count how many times it appears.

def count_occurrences(list, num):
    return list.count(num)

list = [1, 2, 3, 4, 5, 1, 2, 3, 1, 2, 1]
num = int(input("Enter a number: "))
print(count_occurrences(list, num))