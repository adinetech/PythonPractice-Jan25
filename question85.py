## CSV Reader: Write a Python script to read a CSV file and print each row.

import csv

def read_csv(file_name):
    with open(file_name, 'r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            print(row)

read_csv('question85.csv')