from main import add_book, delete_book, update_book, add_author, list_books, get_author_by_book
from database import get_db
from sqlalchemy.orm import Session


def print_menu():
    print("\n--- Bookshop Management ---")
    print("       ")
    print("1. Add a book")
    print("2. Update a book's title")
    print("3. Delete a book")
    print("4. List all books")
    print("5. Find author of a book")
    print("6. Exit")
    print("       ")
    print("--------------------------")


def handle_add_book(db: Session):
    title = input("Enter the book title: ")
    author = input("Enter the author's name: ")
    new_book = add_book(title, author, db)
    print(f'Book added: {new_book.title} by {new_book.author.name}')


def handle_add_author(db: Session):
    name = input("Enter the author's name: ")
    new_author = add_author(name, db)
    print(f'Author added: {new_author.name}')


def handle_update_book(db: Session):
    book_id = int(input("Enter the book ID: "))
    new_title = input("Enter the new title: ")
    updated_book = update_book(book_id, new_title, db)
    print(f'Book updated: {updated_book.title}')


def handle_delete_book(db: Session):
    book_id = int(input("Enter the book ID: "))
    delete_book(book_id, db)
    print(f'Book with ID {book_id} deleted')


def handle_list_books(db: Session):
    books = list_books(db)
    print("\n--- List of Books ---")
    print("       ")
    for book in books:
        print(f'{book.id}: {book.title} by {book.author.name}')
    print("       ")
    print("---------------------")


def handle_get_author_by_book(db: Session):
    book_id = int(input("Enter the book ID: "))
    author = get_author_by_book(book_id, db)
    if author:
        print(f'Author of the book: {author.name}')
    else:
        print("No author found for this book")


def main():
    db: Session = next(get_db())
    while True:
        print_menu()
        choice = input("Enter your choice (1-6): ")
        if choice == '1':
            handle_add_book(db)
        elif choice == '2':
            handle_update_book(db)
        elif choice == '3':
            handle_delete_book(db)
        elif choice == '4':
            handle_list_books(db)
        elif choice == '5':
            handle_get_author_by_book(db)
        elif choice == '6':
            print("Exiting the application.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
