
from abc import ABC,abstractmethod

class Shape(ABC):

    @abstractmethod
    def show(self):
        pass

    def abc(self):
        print("this is method of abstract class")

class Triangle(Shape):

    def show(self):
        print("this is show method of abstract class triangle")

    def abc(self):
        print("this is abc method of subclass triangle")


obj = Triangle()
obj.show()
obj.abc()
