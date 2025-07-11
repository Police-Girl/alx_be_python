from library_system import Book, EBook, PrintBook, Library

def main():
    # Create instances of different book types
    # Ensure the arguments match the corrected __init__ methods in library_system.py
    book1 = Book("Pride and Prejudice", "Jane Austen")
    ebook1 = EBook("Snow Crash", "Neal Stephenson", 500) # Now expects title, author, file_size
    print_book1 = PrintBook("The Catcher in the Rye", "J.D. Salinger", 234) # Now expects title, author, page_count

    # Create a Library instance
    my_library = Library()

    # Add books to the library using the add_book method
    my_library.add_book(book1)
    my_library.add_book(ebook1)
    my_library.add_book(print_book1)

    # List all books in the library using the list_books method
    my_library.list_books()

if __name__ == "__main__":
    main()


