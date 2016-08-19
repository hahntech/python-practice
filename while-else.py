#!/usr/bin/python3

i = 0
my_list = [1, 2, 3, 4, 5, 6]

while i < len(my_list):
    print(str("element #" + str(my_list[i])))
    i += 1
else:
    print("end of elments")

print("Begin section about 'break' and 'continue'")

j = 0
myOtherList = [1, 2, 3, 4, 5, 6]

while j < len(myOtherList):
    if myOtherList[j] == 5:
        j += 1
        break
        # '% 2 == 0' checks for even numbers
    if myOtherList[j] % 2 == 0:
        j += 1
        continue
    print(myOtherList[j])
    j += 1
else:
    print("no element is left to print")

print("begin section 'try-finally'")
i = 0
my_list = [1, 2, 3, 4, 5, 6]

while i < len(my_list):
    try:
        if my_list[i] == 5:
            break
        if my_list[i] % 2 == 0:
            continue
        print(my_list[i])
    finally:
        i += 1
else:
    print("no element is left to print")
    
