class Book:
    def __init__(self, title, author, genre, availability=True):
        self.title = title
        self.author = author
        self.genre = genre
        self.availability = availability

    def __repr__(self):
        return f"{self.title} by {self.author} ({self.genre})"


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, title):
        for book in self.books:
            if book.title == title:
                self.books.remove(book)
                return True
        return False

    def display_books(self):
        if not self.books:
            print("No books in the library.")
        else:
            for book in self.books:
                print(book)

    def search_book(self, keyword):
        found_books = []
        for book in self.books:
            if keyword.lower() in book.title.lower() or keyword.lower() in book.author.lower():
                found_books.append(book)
        return found_books

    def update_availability(self, title, availability):
        for book in self.books:
            if book.title == title:
                book.availability = availability
                return True
        return False


def main():
    library = Library()

    # Sample data
    book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", "Classic")
    book2 = Book("To Kill a Mockingbird", "Harper Lee", "Fiction")
    book3 = Book("1984", "George Orwell", "Science Fiction")
    library.add_book(book1)
    library.add_book(book2)
    library.add_book(book3)

    while True:
        print("\nLibrary Management System\n")
        print("1. Add a book")
        print("2. Remove a book")
        print("3. Display all books")
        print("4. Search for a book")
        print("5. Update availability of a book")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter title: ")
            author = input("Enter author: ")
            genre = input("Enter genre: ")
            new_book = Book(title, author, genre)
            library.add_book(new_book)
            print("Book added successfully.")

        elif choice == "2":
            title = input("Enter title of the book to remove: ")
            if library.remove_book(title):
                print("Book removed successfully.")
            else:
                print("Book not found.")

        elif choice == "3":
            print("\nList of all books in the library:")
            library.display_books()

        elif choice == "4":
            keyword = input("Enter title or author to search: ")
            found_books = library.search_book(keyword)
            if found_books:
                print("\nSearch Results:")
                for book in found_books:
                    print(book)
            else:
                print("No matching books found.")

        elif choice == "5":
            title = input("Enter title of the book to update availability: ")
            availability = input("Enter availability (True/False): ").lower()
            if availability in ['true', 'false']:
                availability = availability == 'true'
                if library.update_availability(title, availability):
                    print("Availability updated successfully.")
                else:
                    print("Book not found.")
            else:
                print("Invalid availability value.")

        elif choice == "6":
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
