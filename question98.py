## Abstract Class: Use the abc module to define an abstract base class Shape with an abstract method area(). Implement subclasses Circle and Rectangle.

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius
    
class Rectangle(Shape):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth
    
circle = Circle(5)
rectangle = Rectangle(5, 10)

print(f"Circle Area: {circle.area()}")
print(f"Rectangle Area: {rectangle.area()}")