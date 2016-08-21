#!/usr/bin/python3

class Cat:
    """ A Loose Representation of a Cat"""
    animal = "cat"

    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
        self.age = 0

    def birth_day(self):
        self.age += 1

    def get_age(self):
        return self.age

    def get_name(self):
        return self.name

class Dog:
    """A Loose Representation of a Dog"""
    animal = "dog"

    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
        self.age = 0

    def birth_day(self):
        self.age += 1

    def get_age(self):
        return self.age

    def get_name(self):
        return self.name

# this if statement caused the code to only run from within this document
# in other words, if it is called from other object the code will not run
if __name__ == '__main__':
    qwerty = Dog("Qwerty", "German Shepperd")
    raul = Cat("Raul", "Siamese")
    while qwerty.get_age() < 9:
        qwerty.birth_day()
    while raul.get_age() < 3:
        raul.birth_day()
    print("My {}, {}, has {} years".format(qwerty.animal, qwerty.get_name(), qwerty.get_age()))
    print("My {}, {}, has {} years".format(raul.animal, raul.get_name(), raul.get_age()))
