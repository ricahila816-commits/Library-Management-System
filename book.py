class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self._is_available = True
    
    @property
    def is_available(self):
        return self._is_available
    
    @is_available.setter
    def is_available(self, value):
        self._is_available = value
    
    def __str__(self):
        status = "Available" if self.is_available else "Borrowed"
        return f"[{self.book_id}] {self.title} by {self.author} - {status}"