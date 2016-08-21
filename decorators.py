#!/usr/bin/python3

# this function is called the "decorator"
def print_args_and_result(target):
    # '*' = variable number of arguments
    def wrapper(*args):
        print("calling {} with arguments:{}".format(target.__name__, str(args)))
        result = target(*args)
        print("{} result: {}".format(target.__name__, str(result)))
        return result
    return wrapper

# using '@' and the funciton name of the decorator tells python3
# to send these functions to the decorator for processing
@print_args_and_result
def power(a, b):
    return a ** b

@print_args_and_result
def root(a, b):
    return a ** (1 / b)

print(power(5, 2))
print(root(9, 2))
