## Dictionary of Squares: Prompt for n and create a dictionary where each key is from 1 to n and each value is the square of the key.

num = int(input("Enter a number: "))
square = {i: i * i for i in range(1, num + 1)}
print(square)