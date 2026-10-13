
class Employee:

    company = "Google"

    def __init__(self,name,salary,dept,role,qualification):
        self.name = name
        self.salary = salary
        self.dept = dept
        self.role = role
        self.qualification = qualification
        print(f"Employee data :")

    def display(self):
        print(f"Company -> {Employee.company}\nName -> {self.name}\nSalary -> {self.salary}\nDept -> {self.dept}\nRole -> {self.role}\nQualification -> {self.qualification}")

    def __del__(self):
        print(f"Employee data completed")

emp1 = Employee("dev",60000,"marketing","manager","MBA")
emp1.display()

