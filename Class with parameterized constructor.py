
class Car:
            # Constructor (Parameterized)
    def __init__(self,brand,color):
        self.brand = brand               # Instance variables
        self.color = color               # Instance variables
        print(f"{self.brand} : Cars data is completed")

     # Create Objects
c1 = Car("Porsche","Navy blue")
c2 = Car("Bugatti","Silver")

     # Display Values
print("Car1 :",c1.brand,c2.color)
print("Car2 :",c2.brand,c2.color)

