
class Company:

    def show(self):
        print("this is company superclass")


class Boss(Company):

    def show(self):
        print("this is boss subclass of company class")


class Employee1(Boss):

     def show(self):
         print("this is employee1 subclass of boss class")

class Employee2(Boss):

    def show(self):
        print("this is employee2 subclass of boss class")

obj1 = Employee1()
obj2 = Employee2()
obj1.show()
obj2.show()
