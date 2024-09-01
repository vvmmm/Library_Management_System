##################################"Library Management System"##########################################

###OVERVIEW########
The Library Management System is a simple Python application that manages a collection of books. It allows users to add books to the library, borrow books, return borrowed books, and view all available books. The system handles errors such as trying to borrow a book that has already been borrowed, adding a duplicate book, or returning a book that wasn't borrowed.

###FEATURES########
Add Books: Add a new book to the library collection.
Borrow Books: Borrow a book from the library. The system checks if the book is available.
Return Books: Return a borrowed book to the library. The system ensures the book was borrowed before allowing a return.
View Available Books: List all the books currently available in the library.

#######Classes and Error Handling#########
#Classes#

Book: Represents a book with attributes like ISBN, title, author, and publication year.
Library: Manages the collection of books. It supports adding, borrowing, and returning books.

#Custom Exceptions#

BookAlreadyExistsError: Raised when trying to add a book that already exists in the library.
BookNotFoundError: Raised when trying to borrow a book that does not exist in the library.
BookAlreadyBorrowedError: Raised when trying to borrow a book that has already been borrowed.
BookNotBorrowedError: Raised when trying to return a book that was not borrowed.
InvalidPublicationYearError: Raised for invalid publication years.

###Installation##############
To set up the Library Management System, follow these steps:

Clone the repository:

>>git clone https://github.com/vvmmm/Library_Management_System.git
>>cd Library_Management_System

####Usage################
To use the Library Management System, you can run the library_management.py script directly or use it as a module in a larger application.

#Example Usage
#Here's an example of how to use the Library Management System in your Python code:

>>from Library_management.library_management import Library, Book

# Create a Library instance
>>library = Library()

# Add books to the library
>>book1 = Book(isbn="1234567890", title="Python Programming", author="John Doe", publication_year=2022)
>>book2 = Book(isbn="0987654321", title="Data Science Essentials", author="Jane Smith", publication_year=2021)

>>library.add_book(book1)
>>library.add_book(book2)

# Borrow a book
>>library.borrow_book("1234567890")

# Return a book
>>library.return_book("1234567890")

# View available books
>>available_books = library.view_available_books()
>>for book in available_books:
>>    print(f"{book.title} by {book.author}")

#### Running Tests####################
To ensure everything is working correctly, run the unit tests provided

>>python -m unittest discover test_Library_management

This command will discover and run all test cases in the test_Library_management directory

#####Contributing############
If you would like to contribute to the project, please fork the repository and submit a pull request. We welcome all contributions, including bug fixes, new features, and documentation improvements.

####Contact#################
For any questions or suggestions, please reach out to the project maintainers:

Vishal Mehta - vmmehta2612002@gmail.com
