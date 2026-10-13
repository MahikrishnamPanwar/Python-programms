
class Car:
         # Class variable
    wheel = 6       # common to all cars

         # Constructor
    def __init__(self,model,color):
        self.model = model           # Instance variable
        self.color = color           # Instance variable
        print(f"Car {self.model} is created")

        # Instance Method
    def display(self):
        print(f"Car details -> Model : {self.model} , Color : {self.color} , Wheel : {Car.wheel}")

        # Another Method
    def drive(self):
        print(f"{self.model} car is driving")

        # Destructor
    def __del__(self):
        print(f"{self.model} car is destroyed")

        # Object creation
car1 = Car("BMW","Red")
car2 = Car("Bugatti","Orange")
car3 = Car("Thar","Black")

        # Accessing Methods/Functions
car1.display()
car1.drive()
car2.display()
car2.drive()
car3.display()
car3.drive()

       # Accessing Class variable
print(f"Total wheels in cars : {Car.wheel}")

