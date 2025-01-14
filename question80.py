## Line Count: Write a program that counts how many lines are in a file.

def line_count(file_name):
    with open(file_name, 'r') as file:
        print(len(file.readlines()))

line_count('question80.py')