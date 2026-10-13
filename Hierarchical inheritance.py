
class Parent:

    def show_parent(self):
        print("this is parent class of hierarchical inheritance")

class Child1(Parent):

    def show_child1(self):
        print("this is child1 class of hierarchical inheritance")

class Child2(Parent):

    def show_child2(self):
        print("this is child2 class of hierarchical inheritance")

obj1 = Child1()
obj2 = Child2()
obj1.show_parent()
obj1.show_child1()
obj2.show_parent()
obj2.show_child2()
