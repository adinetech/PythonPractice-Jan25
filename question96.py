## Magic Methods: Implement a Python class that overloads the __str__ method to return a string representation of the object.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}"
    
person = Person('Ashik', 30)
print(person)