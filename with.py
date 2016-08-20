#!/usr/bin/python3

import csv
# mainly to demonstrate the benifit of using the 'with' statement.
# and that is the 'with' statement automatically closes resources.
my_dictionaries = [
    {"id": 0, "value": 123},
    {"id": 1, "value": 749},
    {"id": 2, "value": 913}
]

with open('/tmp/with_statement.csv', 'w+', newline='') as csv_file:
    head = my_dictionaries[0]
# The trickiest part comes now, we are using a method provided by
# dictionaries that is called keys and returns an iterable containing
# all the keys in our dictionary and then sorting it with the built-in
# function sorted, as we know keys in a dictionary are not always ordered
# the same way, and it could be very chaotic if every time we write in a
# csv the columns are sorted differently.
    keys = sorted([k for k in head.keys()])
    writer = csv.DictWriter(csv_file, fieldnames=keys)
    writer.writeheader()
    for d in my_dictionaries:
        writer.writerow(d)

with open('/tmp/with_statement.csv', 'r+', newline='') as csv_file:
# On the read process there is another weird thing going on with a for
# statement between square brackets. That is called 'for comprehension',
# we are basically building an array of 'd' for every 'd' in an iterable
# (csv.DictReader(csv_file) returns an iterable with every row in our
# csv file).
    read_dictionaries = [ d for d in csv.DictReader(csv_file)]

for d in read_dictionaries:
    print(str(d))
