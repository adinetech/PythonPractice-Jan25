## Count Vowels (Recursive): Write a recursive function that returns the number of vowels in a string.

def count_vowels(string):
    vowels = 'aeiou'
    if len(string) == 0:
        return 0
    else:
        if string[0].lower() in vowels:
            return 1 + count_vowels(string[1:])
        else:
            return count_vowels(string[1:])
        
print(count_vowels('hello'))
print(count_vowels('world'))
print(count_vowels('aeiou'))
print(count_vowels(''))
print(count_vowels('h'))
print(count_vowels('a'))
print(count_vowels('e'))
print(count_vowels('i'))
