## Read File: Write a Python script that reads a text file and prints its contents.

def read_file(file_name):
    with open(file_name, 'r') as file:
        print(file.read())

read_file('question76.py')