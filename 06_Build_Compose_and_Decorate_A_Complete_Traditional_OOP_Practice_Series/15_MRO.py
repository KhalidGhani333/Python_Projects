

# Create four classes:
# A with a method show(),
# B and C that inherit from A and override show(),
# D that inherits from both B and C.
# Create an object of D and call show() to observe MRO.


class A:
    def show(self):
        print("Class A")

class B (A):
    def show(self):
        print("Class B")

class C (A):
    def show(self):
        print("Class C")

class D (B,C):    # Multiple inheritance from B and C
    pass


obj = D()
obj.show()

# Print the MRO
print(D.mro())