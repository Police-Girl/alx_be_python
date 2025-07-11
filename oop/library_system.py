class Book:
	def __init__(self, title, author):
		self.title = title
		self.author = author

class EBook(Book):
	def __str__(self, title, author, file_size):
		super().__init__(title,author) #for self.title and self.author
		#Sself.title = title
		#self.author = author
		self.file_size = file_size #this class's unique attribute.

class PrintBook(Book):
	def __str__(self, title, author, page_count):
		super().__init__(title,author)
		#self.title = title
		#self.author = author
		self.page_count = page_count

#class Library:
	#def list_books(self):
		#self.books = [] #the Library is holding a list of Book objects...
	#def  add_book(self,book):
		#self.books.append(book)
		#print(f"Added '{book.title}' to the library")
class Library:
	def __init__(self): # Added __init__ to initialize books list
		self.books = []

	def add_book(self, book): # Uncommented and ready to use
		self.books.append(book)

	def list_books(self): # Completed list_books method
		if not self.books:
			print("The library currently has no books.")
			return #intentation error manzee

		for book in self.books:
			if isinstance(book, EBook):
				print(f"EBook: {book.title} by {book.author}, File Size: {book.file_size}KB")
			elif isinstance(book, PrintBook):
				print(f"PrintBook: {book.title} by {book.author}, Page Count: {book.page_count}")
			else:
				print(f"Book: {book.title} by {book.author}")

