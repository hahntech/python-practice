#!/usr/bin/python3

def a_function(an_array, a_function_argument):
    return [a_function_argument(item) for item in an_array]

def add_one(n):
    return n + 1

my_array = [5, 6, 7, 8]

print(str(a_function(my_array, add_one)))

# for more information on 'for comprehension' see:
# https://docs.python.org/3.5/howto/functional.html?highlight=comprehension#generator-expressions-and-list-comprehensions
