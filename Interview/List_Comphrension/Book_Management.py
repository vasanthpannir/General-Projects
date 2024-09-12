
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author


class Library:
    def __init__(self):
        self.books = []

    def add_books(self, book):
        self.books.append(book)

    def library_search(self,keyword):
        return [book.author for book in self.books if keyword.lower() in book.author.lower()]


library = Library()
library.add_books(Book("Python_Programming","Jon,Doe"))
library.add_books(Book("Data with python","Vasanth Pannir"))


print("The book containing with the tittle python is",library.library_search("Doe"))


