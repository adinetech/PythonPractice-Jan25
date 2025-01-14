## Class Inheritance: Create a base class Animal and a derived class Dog. Override a method speak() in the Dog class to print "Woof!".

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        print('Woof!')


dog = Dog('Fido')
dog.speak()

