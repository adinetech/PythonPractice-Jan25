## Copy File: Write a Python program to copy the contents of one file to another.

def copy_file(file_name, new_file_name):
    with open(file_name, 'r') as file:
        with open(new_file_name, 'w') as new_file:
            new_file.write(file.read())

copy_file('question78.py', 'question78_copy.py')