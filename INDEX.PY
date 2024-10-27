class Book:
    def __init__(self, title, author):
        """Initialize the book's title and author."""
        self.title = title
        self.author = author

    def display_info(self):
        """Display the book's details."""
        print(f"Title: {self.title}, Author: {self.author}")


class Library:
    def __init__(self):
        """Initialize an empty library."""
        self.books = []

    def add_book(self, book):
        """Add a book to the library."""
        self.books.append(book)

    def display_books(self):
        """Display all books in the library."""
        if not self.books:
            print("No books in the library.")
            return
        print("Books in the library:")
        for book in self.books:
            book.display_info()


class Member:
    def __init__(self, name):
        """Initialize the member's name."""
        self.name = name
        self.borrowed_books = []

    def borrow_book(self, book, library):
        """Borrow a book from the library."""
        if book in library.books:
            self.borrowed_books.append(book)
            library.books.remove(book)
            print(f"{self.name} borrowed '{book.title}'")
        else:
            print(f"'{book.title}' is not available in the library.")

    def return_book(self, book, library):
        """Return a book to the library."""
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
            library.add_book(book)
            print(f"{self.name} returned '{book.title}'")
        else:
            print(f"{self.name} did not borrow '{book.title}'.")

    def display_borrowed_books(self):
        """Display borrowed books."""
        if not self.borrowed_books:
            print(f"{self.name} has not borrowed any books.")
            return
        print(f"{self.name} has borrowed:")
        for book in self.borrowed_books:
            book.display_info()



if __name__ == "__main__":
    
    library = Library()

    
    book1 = Book("1984", "George Orwell")
    book2 = Book("To Kill a Mockingbird", "Harper Lee")

    
    library.add_book(book1)
    library.add_book(book2)

    
    library.display_books()

    
    member = Member("Alice")

    
    member.borrow_book(book1, library)

    
    member.display_borrowed_books()

    member.return_book(book1, library)

    
    library.display_books()
