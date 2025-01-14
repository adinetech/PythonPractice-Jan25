## Frequency of Elements: Count how often each element appears in a list and store the result in a dictionary.

list1 = [1, 2, 3, 4, 5, 1, 2, 3, 1, 2, 1]
frequency = {i: list1.count(i) for i in list1}
print(frequency)

