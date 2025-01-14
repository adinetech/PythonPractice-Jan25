## Palindrome Check (Recursive): Write a recursive function that checks if a string is a palindrome.

def is_palindrome(string):
    if len(string) <= 1:
        return True
    else:
        if string[0] == string[-1]:
            return is_palindrome(string[1:-1])
        else:
            return False
    
print(is_palindrome('hello'))
print(is_palindrome('naman'))
