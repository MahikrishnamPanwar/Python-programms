
class Employee:

    name = 'Meta'

    def display(self):
        name = "Rahul"
        print("this is display method of class employee")
        print(f"this employee name is : {name}")

    print(f"the employee works in : {name}")

emp1 = Employee()
emp1.display()
print(f"the employee works in : {emp1.name}")
 # print(f"the employee name is : {emp1.name}")
