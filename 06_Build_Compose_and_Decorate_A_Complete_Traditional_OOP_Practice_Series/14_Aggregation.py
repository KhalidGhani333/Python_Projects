
# Create a class Department and a class Employee. Use aggregation by having a Department object store a reference to an Employee object that exists independently of it.


class Employee():
    def __init__(self,name):
        self.name = name

    def show(self):
        print(f"Employee name:{self.name}")

class Department:
    def __init__(self,depart_name,employee):
        self.depart_name = depart_name
        self.employee = employee  # Aggregation: reference only
        
    def show_details(self):
        print(f"Department: {self.depart_name}")
        self.employee.show()   # Calling method from Employee
        

emp1 = Employee("Khalid")
depart = Department("IT",emp1)
depart.show_details()