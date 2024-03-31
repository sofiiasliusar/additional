class Parent:
    hair = "brown"
    speaks = ["English"]

class Child(Parent):
    hair = "purple"
    def __init__(self):
        super().__init__()
        self.speaks.append("German") # ** because here we are extendinf self, which refers to an instance

print(Child.hair)
child_instance = Child()
# print(Child.speaks) - accesses from Parent class
print(child_instance.speaks) # accesses from child class **
