
# Use the abc module to create an abstract class Shape with an abstract method area(). Inherit a class Rectangle that implements area().

from abc import ABC ,abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass      # Abstract method, must be implemented in subclasses


class Rectangle(Shape):
    def __init__(self,height,width):
        self.height = height
        self.width = width

    def area(self):
        return self.height * self.width
    
rect = Rectangle(10,4)

print("The Area of Rectangle is ", rect.area())
