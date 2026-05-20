class Member:
    def __init__(self, member_id, name, email):
        self.member_id = member_id
        self.name = name
        self.email = email
        self.borrowed_books = []
    
    def add_borrowed_book(self, book_id):
        self.borrowed_books.append(book_id)
    
    def remove_borrowed_book(self, book_id):
        if book_id in self.borrowed_books:
            self.borrowed_books.remove(book_id)
    
    def __str__(self):
        return f"[{self.member_id}] {self.name} ({self.email}) - Books: {len(self.borrowed_books)}"