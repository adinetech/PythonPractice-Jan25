## Encapsulation: Demonstrate encapsulation by creating a class with private attributes and use getter and setter methods to access/modify them.

class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def set_name(self, name):
        self.__name = name

    def set_age(self, age):
        self.__age = age

person = Person('John', 30)
print(person.get_name())
print(person.get_age())

person.set_name('Ashik')
person.set_age(35)
print(person.get_name())
print(person.get_age())