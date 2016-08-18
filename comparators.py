#!/usr/bin/python3

a = 5
b = 3
c = 2

# True
print(a > b > c)
print(a >= c)
print(a > b > c < a)
print(a == b or c < b)
print(not (a == b and c > a))
print(b != c)
print(a is not None)

print("------------------------")

#False
print(a < b < c)
print(b > 10)
print(b is None and a != 5)
print(not a)
