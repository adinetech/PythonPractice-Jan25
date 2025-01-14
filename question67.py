## Recursive Fibonacci: Implement a function fib(n) to return the nth Fibonacci number using recursion.

def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n - 1) + fib(n - 2)
    
print(fib(0))
print(fib(1))
print(fib(2))
