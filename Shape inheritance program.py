
class Shape:

    def __init__(self,color = 'blue',border_width = 1.0):
        self.__color = color
        self.__border_width = border_width

    def get_color(self):
        return self.__color

    def set_color(self,color):
        self.__color = color

    def get_border_width(self):
        return self.__border_width

    def set_border_width(self,border_width):
        self.__border_width = border_width


class Rectangle(Shape):

    def __init__(self,length,width,color = 'blue',border_width = 1.0):
        super().__init__()
        self.__length = length
        self.__width = width

    def get_length(self):
        return self.__length

    def set_length(self,length):
        self.__length = length

    def get_width(self):
        return self.__width

    def set_width(self,width):
        self.__width = width


class Circle(Shape):

    def __init__(self,radius,color = 'blue',border_width = 1.0):
        super().__init__()
        self.__radius = radius

    def get_radius(self):
        return self.__radius

    def set_radius(self,radius):
        self.__radius = radius


class Triangle(Shape):

    def __init__(self,base,height,color = 'blue',border_width = 1.0):
        super().__init__()
        self.__base = base
        self.__height = height

    def get_base(self):
        return self.__base

    def set_base(self,base):
        self.__base = base

    def get_height(self):
        return self.__height

    def set_height(self,height):
        self.__height = height



t1 = Triangle(5,8)
print(f"the details of triangle are -> Base : {t1.get_base()}, Height : {t1.get_height()}, Color : {t1.get_color()}, Border width : {t1.get_border_width()}")

r1 = Rectangle(6,4,'white',7)
print(f"the details of rectangle are -> Length : {r1.get_length()}, Width : {r1.get_width()}, Color : {r1.get_color()}, Border width : {r1.get_border_width()}")

c1 = Circle(8,'orange',9)
print(f"the details of circle are -> Radius : {c1.get_radius()}, Color : {c1.get_color()}, Border width : {c1.get_border_width()}")

r1.set_color('black')
print(f"the updated color of rectangle -> Color : {r1.get_color()}")

c1.set_radius(10)
print(f"the updated radius of circle : {c1.get_radius()}")

t1.set_height(7)
print(f"the updated height of triangle : {t1.get_height()}")

