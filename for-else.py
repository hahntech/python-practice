#!/usr/bin/python3

my_list = [1, 2, 3, 4, 5, 6]

for item in my_list:
    if item == 5:
        break
    if item % 2 == 0:
        continue
    print(item)
else:
    print("end of elements in list")
    
