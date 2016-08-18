#!/usr/bin/python3

my_dog = {
    "breed": "German Shepperd",
    "name": "Qwerty",
    "age": 9,
    "gender": "MALE"
}

print(str(my_dog))
# second argument to the get method is the default value
# returned in case the key does not exist
my_dog["age"] = my_dog.get("age", 0) + 1
print(str("After get() + 1: " +str(my_dog)))

# an alternative way of handling a potential missing key
if "age" in my_dog:
    my_dog["age"] += 1
else:
    my_dog["age"] = 1

# if condition:
#     action
# elif another condition:
#     another action
# elif another condition:
#     another action
# ...
# else:
#     action if none of the above conditions is met

print(str("After if/else: " + str(my_dog)))

my_dog["girlfriend_name"] = "Quiara"

print(str(my_dog))

del my_dog["girlfriend_name"]

print(str(my_dog))
