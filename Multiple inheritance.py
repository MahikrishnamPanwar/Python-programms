
class Father:

    def show_father(self):
        print("this is father class")

class Mother:

    def show_mother(self):
        print("this is mother class")

class Child(Father,Mother):

    def show_child(self):
        print("this is child class")

child1 = Child()
child1.show_child()
child1.show_father()
child1.show_mother()
