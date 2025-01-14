## Property Decorator: Create a class that uses the @property decorator to get/set an attribute with some validation logic.

class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if name == '':
            raise ValueError('Name cannot be empty')
        self.__name = name

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        if age < 0:
            raise ValueError('Age cannot be negative')
        self.__age = age

person = Person('Ashik', 30)
print(person.name)
print(person.age)