import csv
import json

csv_file_path = 'table_data.csv'
json_file_path = 'data.json'

# Read CSV file and convert to a list of dictionaries
csv_data = []
with open(csv_file_path, 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        csv_data.append(row)

# Write the list of dictionaries to a JSON file
with open(json_file_path, 'w') as json_file:
    json.dump(csv_data, json_file, indent=2)

print(f'Conversion complete. JSON data saved to {json_file_path}')
