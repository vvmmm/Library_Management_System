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
            
#########TEST ADD BOOK INVALID PUBLICATION IN LIBRARY.###############
    def test_add_book_invalid_publication_year(self):
        book = Book(isbn="1234567890", title="Test Book", author="Test Author", publication_year="invalid_year")
        # year must be in Integer data type
        with self.assertRaises(InvalidPublicationYearError):
            self.library.add_book(book)
            
        book = Book(isbn="1234567890", title="Test Book", author="Test Author", publication_year=2025)
        # year must be less then current year 2024
        with self.assertRaises(InvalidPublicationYearError):
            self.library.add_book(book)

#########TEST BORROW BOOK SUCCESSFUL IN LIBRARY.###############
    def test_borrow_book_success(self):
        book = Book(isbn="1234567890", title="Test Book", author="Test Author", publication_year=2023)
        self.library.add_book(book)
        self.library.borrow_book("1234567890")
        self.assertNotIn("1234567890", self.library.books)
        self.assertIn("1234567890", self.library.borrowed_books)

#########TEST BORROW BOOK NOT FOUND IN LIBRARY.###############
    def test_borrow_book_not_found(self):
        with self.assertRaises(BookNotFoundError):
            self.library.borrow_book("1234567890")

#########TEST BORROW BOOK ALREADY BORROWED FROM LIBRARY.###############
    def test_borrow_book_already_borrowed(self):
        book = Book(isbn="1234567890", title="Test Book", author="Test Author", publication_year=2023)
        self.library.add_book(book)
        self.library.borrow_book("1234567890")
        with self.assertRaises(BookAlreadyBorrowedError):
            self.library.borrow_book("1234567890")

#########TEST RETURN BOOK SUCCESSFUL TO LIBRARY.###############
    def test_return_book_success(self):
        book = Book(isbn="1234567890", title="Test Book", author="Test Author", publication_year=2023)
        self.library.add_book(book)
        self.library.borrow_book("1234567890")
        self.library.return_book("1234567890")
        self.assertIn("1234567890", self.library.books)
        self.assertNotIn("1234567890", self.library.borrowed_books)

#########TEST RETURN BOOK NOT BORROWED IN LIBRARY.###############
    def test_return_book_not_borrowed(self):
        book = Book(isbn="1234567890", title="Test Book", author="Test Author", publication_year=2023)
        self.library.add_book(book)
        with self.assertRaises(BookNotBorrowedError):
            self.library.return_book("1234567890")


#########TEST VIEW AVAILABLE BOOKS IN LIBRARY.###############
    def test_view_available_books(self):
        book1 = Book(isbn="1234567890", title="Test Book 1", author="Test Author 1", publication_year=2023)
        book2 = Book(isbn="0987654321", title="Test Book 2", author="Test Author 2", publication_year=2022)
        self.library.add_book(book1)
        self.library.add_book(book2)
        available_books = self.library.view_available_books()
        self.assertEqual(len(available_books), 2)
        self.assertIn(book1, available_books)
        self.assertIn(book2, available_books)

if __name__ == "__main__":
    unittest.main()