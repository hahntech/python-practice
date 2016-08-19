#!/usr/bin/python3

my_numbers = [2, 125, 9, 255, 0]

for n in my_numbers:
    binary_representation = ""
    remain = n
    while remain >= 2:
        binary_representation = str(remain % 2) + binary_representation
        remain //= 2
    binary_representation = str(remain) + binary_representation
    binary_representation = ("0" * (8 - len(binary_representation))) + binary_representation
    print(binary_representation)
else:
    # this is odd. multiply text by a number and it results
    # in the text repeated x number of times
    print("0" * 8) # = "00000000"
