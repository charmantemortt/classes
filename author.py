class Book():
    def __init__(self, title, year):
        self.title = title
        self.year = year

    def __str__(self):
        return(f"{self.title}, {self.year}")

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

    def get_books_by_year(self, year):
        books_list = []
        for book in self.books:
            if book.year == year:
                books_list.append(book.title)
            else:
                print("")
        return(books_list)



author = Author("Lev Tolstoy")
book1 = Book("War and Peace", 1869)
book2 = Book("Anna Karenina", 1877)

author.add_book(book1)
author.add_book(book2)

author.display_books()
print(author.get_books_by_year(1877))
