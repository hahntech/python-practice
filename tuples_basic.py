#!/usr/bin/python3

my_tuple = 1, "a string", 3.5

print(str(my_tuple[0]))

try:
    del my_tuple[1]
except TypeError:
    print("tuples are immutable. del not permitted.")

try:
    my_tuple[1] = 3
except TypeError:
    print("tuples are immutable. assingment not premitted.")

print("Begin section on sets.")

my_set = {"a string", 2, "another string"}
print(str(my_set))

my_set.add(3.5)
print(str(my_set))

print(str(my_set.pop()))
print(str(my_set))

print(str(my_set.pop()))
print(str(my_set))

print(str(my_set.pop()))
print(str(my_set))

print(str(my_set.pop()))
print(str(my_set))

print("Begin section on set operations.")
