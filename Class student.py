
class Student:

    school = "DBA"

    def __init__(self,name,age,Class,section):
        self.name = name
        self.age = age
        self.Class = Class
        self.section = section
        print(f"Student details :")

    def data(self):
        print(f"School -> {Student.school}\nName -> {self.name}\nAge -> {self.age}\nClass -> {self.Class}\nSection -> {self.section}")

    def __del__(self):
        print(f"Details completed")

s1 = Student("Anil",15,"9th","A")
s1.data()

s2 = Student("Priya",12,"6th","B")
s2.data()
