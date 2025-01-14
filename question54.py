## Count Lines in File: Read a file and count how many lines it contains.

def count_lines(file_name):
    with open(file_name, 'r') as file:
        print(len(file.readlines()))

count_lines('question54.py')