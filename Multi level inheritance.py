
class Grandparent:

    def show_grandparent(self):
        print(f"this is grandparent class")

class Parent(Grandparent):

    def show_parent(self):
        print(f"this is parent class")

class Child(Parent):

    def show_child(self):
        print(f"this is child class")


a = Child()
a.show_grandparent()
a.show_parent()
a.show_child()

