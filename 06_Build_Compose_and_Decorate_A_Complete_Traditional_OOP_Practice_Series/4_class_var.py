

# Create a class Car with a public variable brand and a public method start(). Instantiate the class and access both from outside the class.

class Bank:
    bank_name = "Bank AlFalah"

    def __init__(self,customer_name):
        self.customer_name = customer_name

    @classmethod
    def change_bank_name(cls,name):
        cls.bank_name = name

    def display(self):
        print(f"{self.customer_name} Bank is : {self.bank_name}")
    
    
bank1 = Bank("khalid")
bank1.display()

Bank.change_bank_name("National Bank")
bank2 = Bank("Ali")
bank2.display()