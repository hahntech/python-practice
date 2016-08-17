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

setA = set("abcdefg")
setB = {"b", "d", "g", "h"}

print("set A: " + str(setA))
print("set B: " + str(setB))

union = setA.union(setB)
intersection = setA.intersection(setB)
difference = setA.difference(setB)
symmetric_difference = setA.symmetric_difference(setB)

print("Union: " + str(union))
print("Intersection: " + str(intersection))
print("Difference: " + str(difference))
print("Symmetric Difference: " + str(symmetric_difference))

print("a in union: " + str("a" in union))
print("b in difference: " + str("b" in difference))
