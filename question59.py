## Command-Line Arguments: Write a script that takes command-line arguments (e.g., file paths) and prints them.

import sys

def print_args():
    for arg in sys.argv:
        print(arg)

print_args()