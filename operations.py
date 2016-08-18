#!/usr/bin/python3

a = 10
b = 7

sum = a + b
diff = a - b
product = a * b
quotient = a / b
floored_quotient = a // b
remainder = a % b

print(str("sum of a and b: ") + str(sum))
print(str("the difference of a and b: ") + str(diff))
print(str("the product of a and b: ") + str(product))
print(str("the quotient of a / b: ") + str(quotient))
print(str("floored quotient? of a // b: ") + str(floored_quotient))
print(str("the remainder of a % b: ") + str(remainder))

print(str("the absolute value of b - a: ") + str(abs(b - a)))
print(str("the integer of a / b: ") + str(int(a / b)))
print(str("complex? No idea what this is: ") + str(complex(0.3, 5) - complex(1, 2)))
