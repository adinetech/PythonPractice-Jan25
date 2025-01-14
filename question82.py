## Find Longest Word in File: Write a program that finds the longest word in a text file and prints it.

def longest_word(file_name):
    with open(file_name, 'r') as file:
        words = file.read().split()
        longest = max(words, key=len)
        print(longest)

longest_word('question82.py')