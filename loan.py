from datetime import datetime

class Loan:
    _counter = 1
    
    def __init__(self, book_id, member_id):
        self.loan_id = Loan._counter
        Loan._counter += 1
        self.book_id = book_id
        self.member_id = member_id
        self.borrow_date = datetime.now().strftime("%Y-%m-%d %H:%M")
        self.is_returned = False
        self.return_date = None
    
    def mark_returned(self):
        self.is_returned = True
        self.return_date = datetime.now().strftime("%Y-%m-%d %H:%M")
    
    def __str__(self):
        status = "Returned" if self.is_returned else "Active"
        date_info = f"Returned: {self.return_date}" if self.is_returned else f"Borrowed: {self.borrow_date}"
        return f"Loan {self.loan_id}: Book {self.book_id} | Member {self.member_id} | {status} | {date_info}"