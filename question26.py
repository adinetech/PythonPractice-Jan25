## Check Substring: Prompt for a string s and a substring sub. Check if sub is present in s.

def check_substring(s, sub):
    return sub in s

s = input("Enter a string: ")
sub = input("Enter a substring: ")

if check_substring(s, sub):
    print(f"{sub} is a substring of {s}.")
else:
    print(f"{sub} is not a substring of {s}.")