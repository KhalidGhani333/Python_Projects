
# Create a class Product with a private attribute _price. Use @property to get the price,
#  @price.setter to update it, and @price.deleter to delete it.


class Product:
    def __init__(self,price):
        self._price = price

    @property
    def Price(self):
        print("Getting Price...")
        return self._price
    
    @Price.setter
    def Price(self,new_Price):
        print("Setting price...")
        self._price = new_Price
    

    @Price.deleter
    def Price(self):
        print("Price Deleted!")
        del self._price


p = Product(500)
print(p.Price)

p.Price = 600
print(p.Price)

del p.Price