## Search in File: Write a program to search for a specific substring in a file and print the lines where it appears.

def search_in_file(file_name, search_string):
    with open(file_name, 'r') as file:
        for line in file:
            if search_string in line:
                print(line)

search_in_file('question83.py', 'file')