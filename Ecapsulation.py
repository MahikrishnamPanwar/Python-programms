
class Student:

    def __init__(self,name,age,course,marks):
        self.__name = name
        self.__age = age
        self.__course = course
        self.__marks = marks

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def get_course(self):
        return self.__course

    def get_marks(self):
        return self.__marks

    def set_marks(self,marks):
        if 0 <= marks <= 100:
            self.__marks = marks
        else:
            print("invalid marks")

s1 = Student("Shyam",15,"maths",65)
print(f"the student details -> \n Name : {s1.get_name()} , Age : {s1.get_age()} , Course : {s1.get_course()}")
print(f"the student obtained the marks are : {s1.get_marks()}")

s1.set_marks(93)
print(f"the updated marks are : {s1.get_marks()}")
