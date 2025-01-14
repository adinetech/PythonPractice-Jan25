## File Read: Write a program that reads a text file and prints its contents to the screen.

def read_file(file_name):
    with open(file_name, 'r') as file:
        print(file.read())

read_file('question51.py')