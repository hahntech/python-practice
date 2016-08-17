#!/usr/bin/python3

my_dictionary = {
    "name": "Sebastian",
    "age": 21
}

print(str(my_dictionary.get("name")))
print(str(my_dictionary["name"]))
print(str(my_dictionary.get("key that does not exist")))
try:
    print(str(my_dictionary["key that does not exist"]))
except:
    print("Tried to access a key that was not present.")
