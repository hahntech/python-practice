#!/usr/bin/python3

my_list = [1,2,3]

print(str(my_list))

my_list.append(4)

my_list[2] = 5

print(str(my_list))

try:
    my_list[4] = 2
except IndexError:
    print("element at index 4 did not exist.")
    
