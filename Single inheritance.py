
class Parent:

    def show_parent(self):
        print(f"this is parent of parent method")

class Child(Parent):

    def show_child(self):
        print(f"\n this is child of parent method \n")

c1 = Child()
c1.show_parent()
c1.show_child()

c2 = Parent()
c2.show_parent()
# c2.show_child        # this will show error
