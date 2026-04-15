from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def draw(self):
        pass
    
class Circle(Shape):
    def draw(self):
        pass

class Square(Shape):
    def draw(self):
        pass

