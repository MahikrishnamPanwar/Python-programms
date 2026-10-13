
class Shape:

    def area(self):
        print("area of shape")

class Circle(Shape):

    def area(self):
        print("area = circumference")

class Rectangle(Shape):

    def area(self):
        print("area = length * width")

s1 = Shape()
c1 = Circle()
r1 = Rectangle()

for obj in (s1,c1,r1):
    obj.area()

# s1.area()
# c1.area()
# r1.area()

