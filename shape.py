import abc
class Shape(abc.ABC):
    @abc.abstractmethod
    def area(self): pass

class Square(Shape):
    def __init__(self, a):
        self.a = a

    def area(self):
        return self.a**2

    def description(self):
        print("Square area:", square.area())

    def __str__(self):
        print("Square with side:", self.a)

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius**2

    def description(self):
        print("Circle area:", circle.area())

    def __str__(self):
        print("Circle radius:", self.radius)

square = Square(50)
square.description()
square.__str__()

circle = Circle(20)
circle.description()
circle.__str__()
