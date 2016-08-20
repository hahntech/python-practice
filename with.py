#!/usr/bin/python3

import csv

my_dictionaries = [
    {"id": 0, "value": 123},
    {"id": 1, "value": 749},
    {"id": 2, "value": 913}
]

with open('/tmp/with_statement.csv', 'w+', newline='') as csv_file:
    head = my_dictionaries[0]
    keys = sorted([k for k in head.keys()])
    writer = csv.DictWriter(csv_file, fieldnames=keys)
    writer.writeheader()
    for d in my_dictionaries:
        writer.writerow(d)

with open('/tmp/with_statement.csv', 'r+', newline='') as csv_file:
    read_dictionaries = [ d for d in csv.DictReader(csv_file)]

for d in read_dictionaries:
    print(str(d))
