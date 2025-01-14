## Append to File: Write a program that appends a user-input line to an existing file without overwriting it.

def append_file(file_name):
    with open(file_name, 'a') as file:
        file.write(input("Enter a string: "))

append_file('question77.txt')