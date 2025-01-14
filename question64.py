## Polymorphism: Define classes Circle, Square, and Triangle each with a draw() method. Call draw() on a list of shape objects to demonstrate polymorphism.

class Circle:
    def draw(self):
        print('Drawing Circle')

class Square:
    def draw(self):
        print('Drawing Square')

class Triangle:
    def draw(self):
        print('Drawing Triangle')

shapes = [Circle(), Square(), Triangle()]

for shape in shapes:
    shape.draw()