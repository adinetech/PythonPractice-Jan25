## Multiple Classes: Create classes Rectangle and Square. Square should inherit from Rectangle (or implement composition) in a way that automatically sets the length and width to the same value.

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)

square = Square(5)
print(f"Length: {square.length}, Width: {square.width}")