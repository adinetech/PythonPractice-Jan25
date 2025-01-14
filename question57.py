## Find & Replace in File: Search for a specific word in a file and replace it with another word, then overwrite the file with the changes.

def find_replace(file_name, old_word, new_word):
    with open(file_name, 'r') as file:
        text = file.read()
        text = text.replace(old_word, new_word)
    with open(file_name, 'w') as file:
        file.write(text)

find_replace('question57.py', 'question', 'answer')