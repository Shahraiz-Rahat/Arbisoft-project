import pytest
from Libarary_Management_System import Book, Library

@pytest.fixture
def library_with_books():
    library = Library()
    book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", "Classic")
    book2 = Book("To Kill a Mockingbird", "Harper Lee", "Fiction")
    book3 = Book("1984", "George Orwell", "Science Fiction")
    library.add_book(book1)
    library.add_book(book2)
    library.add_book(book3)
    return library

def test_add_book(library_with_books):
    new_book = Book("Test Book", "Test Author", "Test Genre")
    library_with_books.add_book(new_book)
    assert new_book in library_with_books.books

def test_remove_existing_book(library_with_books):
    assert library_with_books.remove_book("To Kill a Mockingbird") == True
    assert library_with_books.books == [Book("The Great Gatsby", "F. Scott Fitzgerald", "Classic"),
                                        Book("1984", "George Orwell", "Science Fiction")]

def test_remove_non_existing_book(library_with_books):
    assert library_with_books.remove_book("Non Existing Book") == False
    assert library_with_books.books == [Book("The Great Gatsby", "F. Scott Fitzgerald", "Classic"),
                                        Book("To Kill a Mockingbird", "Harper Lee", "Fiction"),
                                        Book("1984", "George Orwell", "Science Fiction")]

def test_search_book_by_title(library_with_books):
    assert library_with_books.search_book("Great") == [Book("The Great Gatsby", "F. Scott Fitzgerald", "Classic")]

def test_search_book_by_author(library_with_books):
    assert library_with_books.search_book("Orwell") == [Book("1984", "George Orwell", "Science Fiction")]

def test_update_availability_existing_book(library_with_books):
    assert library_with_books.update_availability("The Great Gatsby", False) == True
    assert library_with_books.books[0].availability == False

def test_update_availability_non_existing_book(library_with_books):
    assert library_with_books.update_availability("Non Existing Book", True) == False
    assert library_with_books.books[0].availability == True
