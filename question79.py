## Word Count in File: Write a Python program that reads a file and counts the number of words in it.

def word_count(file_name):
    with open(file_name, 'r') as file:
        print(len(file.read().split()))

word_count('question79.py')