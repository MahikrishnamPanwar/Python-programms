
class Grandparent:

    def show_grandparent(self):
        print("this is Grandparent class")

class Father(Grandparent):

    def show_father(self):
        print("this is Father class")

class Mother(Grandparent):

    def show_mother(self):
        print("this is Mother class")

class Child1(Father,Mother):

    def show_child1(self):
        print("this is Child1 class")

class Child2(Father,Mother):

    def show_child2(self):
        print("this is Child2 class")

obj1 = Child1()
obj2 = Child2()
obj1.show_grandparent()
obj1.show_child1()
obj1.show_mother()
obj1.show_father()
print(f"\n diff. in both object \n")
obj2.show_grandparent()
obj2.show_child2()
obj2.show_father()
obj2.show_mother()
