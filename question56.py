## Exception Handling: Write a function that attempts to convert a string to an integer, catching any ValueError and printing a custom message.

def convert_to_int(string):
    try:
        return int(string)
    except ValueError:
        print("Invalid input.")

print(convert_to_int("5"))
print(convert_to_int("five"))