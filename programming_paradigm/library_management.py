class Book:
    """A class representing a book in the library."""

    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False

    def check_out(self):
        """Mark the book as checked out."""
        if not self._is_checked_out:
            self._is_checked_out = True

    def return_book(self):
        """Mark the book as available."""
        if self._is_checked_out:
            self._is_checked_out = False

    def is_available(self):
        """Return True if the book is available, False otherwise."""
        return not self._is_checked_out


class Library:
    """A class representing a library holding multiple books."""

    def __init__(self):
        self._books = []

    def add_book(self, book):
        """Add a new Book object to the library."""
        self._books.append(book)

    def check_out_book(self, title):
        """Check out a book by its title, if available."""
        for book in self._books:
            if book.title == title and book.is_available():
                book.check_out()
                return
        # If no available book matches, do nothing (as per expected behavior)

    def return_book(self, title):
        """Return a book by its title."""
        for book in self._books:
            if book.title == title and not book.is_available():
                book.return_book()
                return

    def list_available_books(self):
        """Print all available books in the format 'Title by Author'."""
        for book in self._books:
            if book.is_available():
                print(f"{book.title} by {book.author}")
