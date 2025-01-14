## Fibonacci Sequence: Print the first n Fibonacci numbers using iteration.

def fibonacci(n):
    a = 0
    b = 1
    for i in range(n):
        print(a, end = " ")
        a, b = b, a + b

fibonacci(int(input("Enter a number: ")))