## Operator Overloading: Define a class Point(x, y) that overloads the + operator to add the coordinates of two Point objects.

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, point):
        return Point(self.x + point.x, self.y + point.y)

    def __str__(self):
        return f'({self.x}, {self.y})'
    
point1 = Point(1, 2)
point2 = Point(3, 4)
point3 = point1 + point2
print(point3)