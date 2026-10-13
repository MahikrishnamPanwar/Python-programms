
class Car:
      # Class attribute
    wheel = 4

    def __init__(self,name,color):
          # Instance attributes
          self.name = name
          self.color = color

       # Create objects
c1 = Car("Lexus","Gold")
c2 = Car("Mercedes_Benz","White")

    # Accessing attributes
print("Class attribute :",Car.wheel)
print("Car1 :",c1.name,c1.color,c1.wheel)
print("Car2 :",c2.name,c2.color,c2.wheel)

