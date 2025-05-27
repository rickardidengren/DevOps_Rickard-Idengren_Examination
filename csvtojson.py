import csv
import json

csvFile = 'Profiles1.csv'
jsonFile = 'data.json'

with open('Profiles1.csv', mode='r', encoding='utf-8') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    data = list(csv_reader)

with open ('data.json', mode='w', encoding='utf-8') as json_file:
    json.dump(data, json_file, indent=4, ensure_ascii=False)

print(f"'{csvFile}' is converted to '{jsonFile}'")