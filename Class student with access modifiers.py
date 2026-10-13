
class Student:

    school_name = "SVVP"

    def __init__(self,name,clas,section,hindi,english,maths,percentage):
        self.name = name
        self.clas = clas
        self.section = section
        self._hindi = hindi
        self._english = english
        self._maths = maths
        self.__percentage = percentage

    def show(self):
        print(f"the details of student ->\n Name : {self.name} , Class : {self.clas} , Section : {self.section}")

    def get(self):
        return self._hindi

    def get1(self):
        return self._english

    def get2(self):
        return self._maths

    def get3(self):
        return self.__percentage

    def set(self,percentage):
        if 0 < percentage < 100:
            self.__percentage = percentage
        else:
            print("invalid marks")

s1 = Student("Sam Wilson","10th","A",63,55,73,91)
print(f"the student studies in : {Student.school_name}")
s1.show()
print(f"Marks in hindi : {s1.get()}")
print(f"Marks in english : {s1.get1()}")
print(f"Marks in maths : {s1.get2()}")
print(f"Percentage : {s1.get3()}%")
s1.set(95)
print(f"the updated percentage : {s1.get3()}%")

