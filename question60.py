## JSON Read & Write: Read data from a JSON file, modify a value, and write the updated data back to the file.

import json

def read_json(file_name):
    with open(file_name, 'r') as file:
        data = json.load(file)
        print(data)
        data['age'] = 30
    with open(file_name, 'w') as file:
        json.dump(data, file)

read_json('question60.json')