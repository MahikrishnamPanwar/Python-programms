
class Vehicle:

    def max_speed(self):
        print("vehicles max speed depends on it's type")

class Car(Vehicle):

    def max_speed(self):
        print("max speed of car is : 350 km/h")

class Bike(Vehicle):

    def max_speed(self):
        print("max speed of bike is : 150 km/h")

class Truck(Vehicle):

    def max_speed(self):
        print("max speed of truck is : 250 km/h")

v = Vehicle()
c = Car()
b = Bike()
t = Truck()

for obj in (v,c,b,t):
    obj.max_speed()
