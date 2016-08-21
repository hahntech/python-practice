#!/usr/bin/python3

class Animal:

    """A Loose Representation of an Animal"""

    def __init__(self, animalType, name, breed):
        self.animalType = animalType
        self.name = name
        self.breed = breed
        self.age = 0

    def birthDay(self):
        self.age +=1

    def getAge(self):
        return self.age

    def getName(self):
        return self.name

class Dog(Animal):
    """A Loose Representation of a Dog"""
    def __init__(self, name, breed):
        Animal.__init__(self, "dog", name, breed)

class Cat(Animal):
    """A Loose Representation of a Cat"""
    def __init__(self, name, breed):
        Animal.__init__(self, "cat", name, breed)

if __name__ == '__main__':
    qwerty = Dog("Qwerty", "German Shepperd")
    while qwerty.getAge() < 9:
        qwerty.birthDay()
    raul = Cat("Raul", "Siamese")
    while raul.getAge() < 3:
        raul.birthDay()
    print("My {}, {}, has {} years".format(qwerty.animalType, qwerty.getName(), qwerty.getAge()))
    print("My {}, {}, has {} years".format(raul.animalType, raul.getName(), raul.getAge()))
