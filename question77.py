## Write File: Write a program that prompts the user for a line of text and writes that line to a file.

def write_file(file_name):
    with open(file_name, 'w') as file:
        file.write(input("Enter a string: "))

write_file('question77.txt')