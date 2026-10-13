
class Car:

    wheel = 4            # Class variable

    def __init__(self,brand,model,colour,year):      # Constructor
        self.brand = brand                           # Instance variable
        self.model = model                           # Instance variable
        self.colour = colour                         # Instance variable
        self.year = year                             # Instance variable
        print(f"Cars details : ")

    def show(self):                # Method/Function
            print(f"Brand : {self.brand}\nModel : {self.model}\nColour : {self.colour}\nYear : {self.year}\nWheels : {Car.wheel}")

    def __del__(self):             # Destructor
        print(f"Cars details completed")

c1 = Car("BMW","xl25","Blue",2025)       # Object creation
c1.show()

c2 = Car("Tata","BE6a","Red",2026)       # Object creation
c2.show()
