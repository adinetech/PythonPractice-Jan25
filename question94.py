## Polymorphism: Demonstrate polymorphism by defining a method draw() in multiple classes (Circle, Triangle, etc.) and calling draw() on a list of shapes.

class Circle:
    def draw(self):
        print("Drawing Circle")

class Triangle:
    def draw(self):
        print("Drawing Triangle")

class Square:
    def draw(self):
        print("Drawing Square")

shapes = [Circle(), Triangle(), Square()]

for shape in shapes:
    shape.draw()