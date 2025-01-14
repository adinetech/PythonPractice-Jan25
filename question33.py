## Prime Check: Write a function is_prime(num) that checks if a number is prime.

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

num = int(input("Enter a number: "))
print(is_prime(num))