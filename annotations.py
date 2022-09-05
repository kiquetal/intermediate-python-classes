import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_magnitude(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def __repr__(self):
        return f"Point(x={self.x}, y={self.y})"


p = Point(2, 3)
print(p.get_magnitude())
print(p)
# Point.get_magnitude(P) => under the hood you can call p.get_magnitude())
