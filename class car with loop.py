
class Car:

    def __init__(self,brand,model,year):
        self.brand = brand
        self.model = model
        self.year = year
       # print(f"Car details ")

    def show(self):
        print(f"Cars details -> Brand : {self.brand} , Model : {self.model}  , Year : {self.year} ")

    def __del__(self):
        print(f"Cars details completed")

c1 = Car("bmw","ss",2022)
c2 = Car("suv","7oo",2025)
c3 = Car("Thar","roxx",2023)

for i in (c1,c2,c3):
    i.show()

# cars_data = [['Toyota','Xe',2014],['Hyundai','XXL',2012],['BMW','X5',2022],['Audi','A6',2023]]
#
# cars = []
#
# for i in cars_data:
#      car = Car(i[0],i[1],i[2])
#      cars.append(car)
#
# print(f"WELCOME TO THE SHOWROOM \n")
# print(f"total cars : {len(cars)}")
# print(f"\n the Details of all Cars \n")
#
# for car in cars:
#     car.show()


