## Replace Character: Prompt for a string and replace all occurrences of a specific character with another.

def replace_char(string, old_char, new_char):
    return string.replace(old_char, new_char)

string = input("Enter a string: ")
old_char = input("Enter the character to replace: ")
new_char = input("Enter the new character: ")
print(replace_char(string, old_char, new_char))