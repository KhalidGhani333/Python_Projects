
# Create a class Student with attributes name and marks. Use the self keyword to initialize these values via a constructor. Add a method display() that prints student details.


class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
    
    def display(self):
        return f"{self.name} got {self.marks} marks in Final Exam."

s1 = Student("Ali" , 511)
print(s1.display())