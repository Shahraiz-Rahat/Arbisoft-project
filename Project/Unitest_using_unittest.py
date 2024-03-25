import unittest
from Libarary_Management_System import Book, Library

class TestLibraryManagementSystem(unittest.TestCase):
    def setUp(self):
        self.library = Library()
        self.book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", "Classic")
        self.book2 = Book("To Kill a Mockingbird", "Harper Lee", "Fiction")
        self.book3 = Book("1984", "George Orwell", "Science Fiction")
        self.library.add_book(self.book1)
        self.library.add_book(self.book2)
        self.library.add_book(self.book3)

    def test_add_book(self):
        new_book = Book("Test Book", "Test Author", "Test Genre")
        self.library.add_book(new_book)
        self.assertIn(new_book, self.library.books)

    def test_remove_existing_book(self):
        self.assertTrue(self.library.remove_book("To Kill a Mockingbird"))
        self.assertNotIn(self.book2, self.library.books)

    def test_remove_non_existing_book(self):
        self.assertFalse(self.library.remove_book("Non Existing Book"))

    def test_search_book_by_title(self):
        result = self.library.search_book("Great")
        self.assertIn(self.book1, result)
        self.assertNotIn(self.book2, result)
        self.assertNotIn(self.book3, result)

    def test_search_book_by_author(self):
        result = self.library.search_book("Orwell")
        self.assertNotIn(self.book1, result)
        self.assertNotIn(self.book2, result)
        self.assertIn(self.book3, result)

    def test_update_availability_existing_book(self):
        self.assertTrue(self.library.update_availability("The Great Gatsby", False))
        self.assertFalse(self.book1.availability)

    def test_update_availability_non_existing_book(self):
        self.assertFalse(self.library.update_availability("Non Existing Book", True))

if __name__ == "__main__":
    unittest.main()