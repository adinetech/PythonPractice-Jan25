## File Copy: Copy the contents of one text file to another.

def copy_file(file_name, new_file_name):
    with open(file_name, 'r') as file:
        with open(new_file_name, 'w') as new_file:
            new_file.write(file.read())

copy_file('question53.py', 'question53_copy.py')