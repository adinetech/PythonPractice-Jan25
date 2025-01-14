## Sum of Digits: Prompt the user for a number (as a string) and compute the sum of its digits.

def sum_of_digits(num):
    return sum([int(i) for i in num])

print(sum_of_digits(input("Enter a number: ")))