## File Write: Prompt the user for a string and write it to a new text file.

def write_file(file_name):
    with open(file_name, 'w') as file:
        file.write(input("Enter a string: "))

write_file('question52.txt')