## Handle File Exceptions: Modify the file-reading program to handle exceptions (e.g., file not found) gracefully.

def read_file(file_name):
    try:
        with open(file_name, 'r') as file:
            print(file.read())
    except FileNotFoundError:
        print('File not found.')
    except Exception as e:
        print('An error occurred:', e)

read_file('question80.py')