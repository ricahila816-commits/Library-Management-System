from book import Book
from member import Member
from loan import Loan
from exceptions import *

class LibraryService:
    def __init__(self):
        self.books = {}
        self.members = {}
        self.loans = []

    def add_book(self, book_id, title, author):
        if book_id in self.books:
            raise BookAlreadyExistsError(f"Book ID {book_id} already exists")
        self.books[book_id] = Book(book_id, title, author)
        return "Book added successfully"

    def register_member(self, member_id, name, email):
        if member_id in self.members:
            raise InvalidInputError(f"Member ID {member_id} already exists")
        self.members[member_id] = Member(member_id, name, email)
        return "Member registered successfully"

    def borrow_book(self, book_id, member_id):
        if book_id not in self.books:
            raise BookNotFoundError(f"Book ID {book_id} not found")
        if member_id not in self.members:
            raise MemberNotFoundError(f"Member ID {member_id} not found")
        
        book = self.books[book_id]
        if not book.is_available:
            raise BookUnavailableError(f"Book '{book.title}' is already borrowed")
        
        book.is_available = False
        self.members[member_id].add_borrowed_book(book_id)
        
        loan = Loan(book_id, member_id)
        self.loans.append(loan)
        return f"Book '{book.title}' borrowed by {self.members[member_id].name}"

    def return_book(self, book_id):
        if book_id not in self.books:
            raise BookNotFoundError(f"Book ID {book_id} not found")
        
        book = self.books[book_id]
        if book.is_available:
            raise BookUnavailableError(f"Book '{book.title}' is not borrowed")

        active_loan = next(
            (loan for loan in self.loans 
             if loan.book_id == book_id and not loan.is_returned), 
            None
        )
        if not active_loan:
            raise BookUnavailableError(f"No active loan found for book '{book.title}'")

        active_loan.mark_returned()
        book.is_available = True
        self.members[active_loan.member_id].remove_borrowed_book(book_id)
        
        return f"Book '{book.title}' returned successfully by {self.members[active_loan.member_id].name}"

    def view_books(self):
        if not self.books:
            return "No books in library"
        return "\n".join(str(book) for book in self.books.values())

    def view_members(self):
        if not self.members:
            return "No members registered"
        return "\n".join(str(member) for member in self.members.values())

    def view_loans(self):
        if not self.loans:
            return "No loan records"
        return "\n".join(str(loan) for loan in self.loans)