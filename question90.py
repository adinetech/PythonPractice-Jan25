## Inheritance: Create a base class Animal and a derived class Dog. The Dog class should inherit attributes and methods from Animal.

class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

class Dog(Animal):
    def __init__(self, name, species, breed):
        super().__init__(name, species)
        self.breed = breed

dog = Dog('Buddy', 'Dog', 'Golden Retriever')
print(f"Name: {dog.name}, Species: {dog.species}, Breed: {dog.breed}")