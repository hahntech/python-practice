#!/usr/bin/python3

# this method can cause unexpected results if you miss the fact
# that each time the funciton is called it is appending new values
# to the array argument
def append_to(item, array=[]):
    array.append(item)
    return array

print(append_to(1))
print(append_to(2))
print(append_to(3))
print(append_to(2, [1]))
print(append_to(4))

# this is a safer and more intuitive way to provide a mutable default
# parameter
def append_to(item, array=[]):
    return array + [item]

print(append_to(1))
print(append_to(2))
print(append_to(2, []))
print(append_to(3))
