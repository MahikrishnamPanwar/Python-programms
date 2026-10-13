
class Cars:

    wheels = 4

    def __init__(self, brand, color):

        self.brand = brand
        self.color = color

    def display(self):
        print(f"The {self.brand} is of {self.color} color")

    @classmethod
    def change_wheels(cls,num):
        cls.wheels = num

    @staticmethod
    def welcome():
        print("Welcome to car showroom")

Cars.welcome()
car1 = Cars('Hyundai','red')
car1.display()
car2 = Cars("BMW", "blue")
car2.display()
Cars.change_wheels(5)
print("Total wheels now:", Cars.wheels)

