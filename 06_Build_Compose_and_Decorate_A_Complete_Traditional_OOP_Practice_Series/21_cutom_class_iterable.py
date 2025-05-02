

# Create a class Countdown that takes a start number. Implement __iter__() and __next__() to make
#  the object iterable in a for-loop, counting down to 0.


class CountDown:
    def __init__(self,start):
        self.start = start

    def __iter__(self):
        self.current = self.start
        return self

    def __next__(self):
        if self.current < 0:
            raise StopIteration
        value = self.current
        self.current -=1
        return value
    
counter = CountDown(5)

for number in counter:
    print(number)