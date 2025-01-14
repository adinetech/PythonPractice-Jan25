## Method Overriding: In the Dog class, override a method speak defined in Animal (e.g., Animal says “Some sound”, but Dog says “Woof!”).

class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def speak(self):
        print("Some sound")

class Dog(Animal):
    def __init__(self, name, species, breed):
        super().__init__(name, species)
        self.breed = breed

    def speak(self):
        print("Woof!")

dog = Dog('Buddy', 'Dog', 'Golden Retriever')
dog.speak()