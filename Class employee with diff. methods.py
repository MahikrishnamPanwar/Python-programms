
class Employee:

    company = "Tesla"

    def __init__(self,name,age,salary,role,department,qualification):
        self.name = name
        self.age = age
        self.salary = salary
        self.role = role
        self.department = department
        self.qualification = qualification
        print(f"{self.name} employee works in : {Employee.company}")

    def detail(self):
        print(f"the details of employee :\nName : {self.name}\nAge : {self.age}\nQualification : {self.qualification}")

    def display(self):
        print(f"the employee works in department : {self.department}")
        print(f"the role of employee in department is : {self.role}")

    def show(self):
        print(f"the salary of employee is : {self.salary}")

    @classmethod
    def change_salary(cls,num):
        cls.salary = num
        print(f"the salary of employee after increment : {num}")

    @classmethod
    def change_role(cls,update):
        cls.role = update
        print(f"the role after promotion : {update}")

    @staticmethod
    def comp():
        print(f"the name of company is : {Employee.company}")

    def __del__(self):
        print(f"{self.name} the details of employee works in {Employee.company} are completed")


emp1 = Employee("Rahul",25,85000,"sales manager","Marketing","B.tech-CS")
emp1.comp()
emp1.detail()
emp1.display()
emp1.show()
emp1.change_salary(200000)
emp1.change_role("Product Manager")


