
# Create a class Counter that keeps track of how many objects have been created. Use a class variable and a class method with cls to manage and display the count.


class Counter:
    objects = 0     # Class variable

    def __init__(self):
        Counter.objects += 1

    @classmethod
    def display(cls):
        return f"Total objects created: {cls.objects}"
    
count = Counter()
count1 = Counter()
count2 = Counter()
print(count.display())
