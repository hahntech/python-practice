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
my_dog["girlfriend_name"] = "Quiara"

print(str(my_dog))

del my_dog["girlfriend_name"]

print(str(my_dog))

print("This section begins a key check demo.")
