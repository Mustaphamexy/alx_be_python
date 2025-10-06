class Book: 
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_checked_out = False
    
    def check_out(self):
        if not self.is_checked_out:
            self.is_checked_out = True
            return True
        return False
    def return_book(self):
        if self.is_checked_out:
            self.is_checked_out = False
            return True
        return False
    def is_available(self):
        return not self.is_checked_out
    
    def __str__(self):
        return f"{self.title} by {self.author}"
    

class Library:
    def __init__(self):
        self._books = []
    def add_book(self, book):
        if isinstance(book, Book):
            self.books.append(book)

    def check_out_book(self, title):
        for book in self.books:
            if book.title == title and book.is_available():
                 if book.check_out():
                    print(f"Successfully checked out: {title}")
                    return True
            else:
                print(f"Book '{title}' is already checked out")
                return False
        print(f"Book '{title}' not found or not available")
        return False
    
    def return_book(self, title):
        """Return a book by title"""
        for book in self.books:
            if book.title == title and not book.is_available():
                if book.return_book():
                    print(f"Successfully returned: {title}")
                    return True
                else:
                    print(f"Book '{title}' is already available")
                    return False
        print(f"Book '{title}' not found or already available")
        return False
    def list_available_books(self):
        """List all available books in the library"""
        available_books = [book for book in self.books if book.is_available()]
        
        if not available_books:
            print("No available books in the library")
        else:
            for book in available_books:
                print(book)
                


 