## Simple Class: Define a class Person with attributes name and age. Create an instance of this class and print its attributes.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

person = Person('John', 30)
print(person.name)