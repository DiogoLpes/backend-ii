from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius ** 2

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

def shape_factory(shape_type, **kwargs):
    if shape_type == "circle":
        return Circle(**kwargs)
    elif shape_type == "square":
        return Square(**kwargs)
    else:
        raise ValueError("Unknown shape type")

# Example usage
circle = shape_factory("circle", radius=5)
print(circle.area())  # 78.53975

square = shape_factory("square", side=4)
print(square.area())  # 16