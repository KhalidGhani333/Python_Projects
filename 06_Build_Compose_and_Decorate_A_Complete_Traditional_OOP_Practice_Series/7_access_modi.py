

# Create a class Employee with:
# a public variable name,
# a protected variable _salary, and
# a private variable __ssn.
# Try accessing all three variables from an object of the class and document what happens.


class Employee:
    def __init__(self,name,salary,ssn):
        self.name = name
        self._salary = salary
        self.__ssn = ssn


emp1 = Employee("Khalid",50000,"0312345678")

print("public : " ,emp1.name)
print("protected : " ,emp1._salary)

try:
    print("protected : " ,emp1.__ssn)

except AttributeError as e:
    print("Private cannot access directly",e)

print("Private using name mangling :", emp1._Employee__ssn)