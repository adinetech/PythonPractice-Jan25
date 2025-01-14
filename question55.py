## CSV Reader: Write a script that reads a CSV file and prints each row.

import csv

def read_csv(file_name):
    with open(file_name, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)

read_csv('question55.csv')