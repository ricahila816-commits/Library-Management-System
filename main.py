from library_service import LibraryService
from exceptions import *

def main():
    lib = LibraryService()
    
    while True:
        try:
            print("\n===== LIBRARY SYSTEM =====")
            print("1. Add Book")
            print("2. Register Member")
            print("3. Borrow Book")
            print("4. Return Book")
            print("5. View Books")
            print("6. View Members")
            print("7. View Loans")
            print("8. Exit")
            
            choice = input("Choose an option: ").strip()

            if choice == '1':
                book_id = input("Enter Book ID: ").strip()
                title = input("Enter Title: ").strip()
                author = input("Enter Author: ").strip()
                print(lib.add_book(book_id, title, author))
            
            elif choice == '2':
                member_id = input("Enter Member ID: ").strip()
                name = input("Enter Name: ").strip()
                email = input("Enter Email: ").strip()
                print(lib.register_member(member_id, name, email))
            
            elif choice == '3':
                book_id = input("Enter Book ID: ").strip()
                member_id = input("Enter Member ID: ").strip()
                print(lib.borrow_book(book_id, member_id))
            
            elif choice == '4':
                book_id = input("Enter Book ID: ").strip()
                print(lib.return_book(book_id))
            
            elif choice == '5':
                print("\n--- Books List ---")
                print(lib.view_books())
            
            elif choice == '6':
                print("\n--- Members List ---")
                print(lib.view_members())
            
            elif choice == '7':
                print("\n--- Loans ---")
                print(lib.view_loans())
            
            elif choice == '8':
                print("Exiting system...")
                break
            
            else:
                print("Invalid choice. Try again.")

        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()