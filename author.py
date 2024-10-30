class Book():
    def __init__(self, title, year):
        self.title = title
        self.year = year

class Author(Book):
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def display_books(self):
        if self.books:
            for book in self.books:
                print(book)
        else:
            print("Error")

    # def get_books_by_year(self, year):

author = Author("Lev Tolstoy")
book1 = Book("War and Peace", 1869)
book2 = Book("Anna Karenina", 1877)

author.add_book(book1)
author.add_book(book2)

author.display_books()

