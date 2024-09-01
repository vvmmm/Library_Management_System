import unittest
from Library.library import Library, Book, BookAlreadyExistsError, BookNotFoundError, BookAlreadyBorrowedError, BookNotBorrowedError, InvalidPublicationYearError

class TestLibraryManagement(unittest.TestCase):

    def setUp(self):
        self.library = Library()

#########TEST ADD BOOK SUCCESSFUL IN LIBRARY.###############

    def test_add_book_success(self):
        book = Book(isbn="1234567890", title="Test Book", author="Test Author", publication_year=2023)
        self.library.add_book(book)
        self.assertIn("1234567890", self.library.books)

#########TEST ADD BOOK DUPLICATE IN LIBRARY.###############
    def test_add_book_duplicate(self):
        book = Book(isbn="1234567890", title="Test Book", author="Test Author", publication_year=2023)
        self.library.add_book(book)
        with self.assertRaises(BookAlreadyExistsError):
            self.library.add_book(book)