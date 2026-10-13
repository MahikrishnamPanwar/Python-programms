

class Student:
    college = "DAVV"

    def __init__(self,name,age,course):
        self.name = name
        self.age = age
        self.course = course
        print(f"student data created")

    def data(self):
        print(f"College : {Student.college}\nName : {self.name}\nAge : {self.age}\nCourse : {self.course}")

    def __del__(self):
        print(f"student data deleted")

S1 = Student("Rahul",20,"B.tech")
S1.data()
S2 = Student("Priya",21,"BCA")
S2.data()
