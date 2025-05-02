

# Create a class Book with a class variable total_books. Add a class method increment_book_count() to increase the count when a new book is added.

class Book:
    total_books = 0

    def __init__(self,title):
        self.title = title
        Book.increment_book_count()
        print(f"{self.title} Book Object Created")
        
    @classmethod
    def increment_book_count(cls):
        cls.total_books +=1
        
        

obj1 = Book("Python")
obj2 = Book("TypeScript")
obj3 = Book("NextJs")

print(f"Total Books added: {Book.total_books}")