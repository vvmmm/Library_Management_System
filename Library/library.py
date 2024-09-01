#Exception raised when trying to add a book that already exists in the library.
class BookAlreadyExistsError(Exception):
    pass

#Exception raised when trying to borrow a book that does not exist in the library.
class BookNotFoundError(Exception):
    pass

#Exception raised when trying to borrow a book that has already been borrowed.
class BookAlreadyBorrowedError(Exception):
    pass

# Exception raised when trying to return a book that was not borrowed.
class BookNotBorrowedError(Exception):
    pass

#Exception raised for invalid publication years.
class InvalidPublicationYearError(Exception):
    pass

class Book:
    def __init__(self, isbn, title, author, publication_year):
        
        self.isbn = isbn
        self.title = title
        self.author = author
        self.publication_year = publication_year

class Library:
    def __init__(self):

        self.books = {}  # Dictionary to hold books with ISBN as key
        self.borrowed_books = set()  # Set to hold borrowed book ISBNs

#############ADD BOOK TO LIBRARY#############################
    def add_book(self, book):
        """
        Raises:
            BookAlreadyExistsError: If the book already exists in the library.
            TypeError: If the input is not a Book instance.
            InvalidPublicationYearError: If the publication year is invalid (not an integer or in the future).
        """
        if not isinstance(book, Book):
            raise TypeError("Only Book instances can be added")

        if book.isbn in self.books:
            raise BookAlreadyExistsError("Book already exists in the library") 

        if not isinstance(book.publication_year, int):
            raise InvalidPublicationYearError("Publication year must be an integer")

        if book.publication_year > 2024:  # Assuming current year is 2024 for this example
            raise InvalidPublicationYearError("Publication year must be less than or equal to the current year")

        self.books[book.isbn] = book

################# BORROW BOOK FROM LIBRARY.###################
    def borrow_book(self, isbn):
        """
        Raises:
            BookNotFoundError: If the book is not available.
            BookAlreadyBorrowedError: If the book is already borrowed.
        """
        if isbn in self.borrowed_books:
            raise BookAlreadyBorrowedError("Book already borrowed")
        if isbn not in self.books:
            raise BookNotFoundError("Book not available")

        # Remove the book from available books and add it to borrowed books
        del self.books[isbn]
        self.borrowed_books.add(isbn)